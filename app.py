from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
import os
import pinecone 
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import streamlit as st

DATA_DIR = 'data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def doc_preprocessing():
    loader = DirectoryLoader(
        DATA_DIR,
        glob='**/*.pdf',     # only the PDFs
        show_progress=True
    )
    docs = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=0
    )
    docs_split = text_splitter.split_documents(docs)
    return docs_split

@st.cache_resource
def embedding_db(PINECONE_API_KEY, PINECONE_ENV):
    embeddings = OpenAIEmbeddings()
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_ENV
    )
    docs_split = doc_preprocessing()
    doc_db = Pinecone.from_documents(
        docs_split, 
        embeddings, 
        index_name='pdf-qanda'
    )
    return doc_db

def retrieval_answer(query, llm, doc_db):
    qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type='stuff',
    retriever=doc_db.as_retriever(),
    )
    result = qa.run(query)
    return result

def main():
    st.title("Question and Answering App powered by LLM and Pinecone")

    PINECONE_API_KEY = st.sidebar.text_input('Enter your Pinecone API key')
    PINECONE_ENV = st.sidebar.text_input('Enter your Pinecone Environment')
    OPENAI_API_KEY = st.sidebar.text_input('Enter your OpenAI API key')

    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

    uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type=['pdf'])

    if uploaded_files:
        for file in uploaded_files:
            file_path = os.path.join(DATA_DIR, file.name)
            with open(file_path, 'wb') as f:
                f.write(file.getbuffer())

        llm = ChatOpenAI()
        doc_db = embedding_db(PINECONE_API_KEY, PINECONE_ENV)

        text_input = st.text_input("Ask your query...") 
        if st.button("Ask Query"):
            if len(text_input)>0:
                st.info("Your Query: " + text_input)
                answer = retrieval_answer(text_input, llm, doc_db)
                st.success(answer)

if __name__ == "__main__":
    main()
