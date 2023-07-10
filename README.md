# PDF Question and Answering App

Welcome to the PDF_QandA GitHub repository! This application is designed to handle question and answering tasks using documents uploaded as PDF files. It leverages powerful natural language processing libraries, including Langchain, Pinecone, and OpenAI, to process, vectorize, and retrieve answers from the text.

## Features

1. **PDF File Uploads**: Users can upload multiple PDF files which the app uses as the knowledge base to answer queries.
2. **Question Answering Interface**: The app provides an interface where users can input queries related to the uploaded documents.
3. **Pinecone Integration**: The app uses Pinecone for vector representation and efficient querying of data.
4. **OpenAI Embeddings**: The app leverages OpenAI's powerful language model to generate embeddings.

## Installation

Clone this repository:

```bash
git clone https://github.com/danielramandi/PDF_QandA.git

Navigate to the cloned repository:

```bash

cd PDF_QandA

Create a virtual environment:

```bash

python3 -m venv env

Activate the virtual environment:

```bash
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install the required dependencies:

```bash
pip install -r requirements.txt

# Usage

Ensure you have the following keys ready:

    Pinecone API key
    Pinecone environment
    OpenAI API key

These keys can be input in the sidebar of the app.

Then, run the Streamlit app:

```bash

streamlit run app.py

Upload PDF files and use the text box to ask your query. The app will generate an answer from the uploaded documents.
Contribution

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.
Links

    Project repository: https://github.com/danielramandi/PDF_QandA
