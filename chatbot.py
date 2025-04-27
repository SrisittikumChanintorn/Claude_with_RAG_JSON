import os
import sys
import json
from typing import overload
from langchain_core.documents import Document

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_anthropic import ChatAnthropic
from langchain_openai import OpenAIEmbeddings 



@overload
def extract_data(path: str, main_key: str)->list[Document]:...

@overload
def extract_data(path: str)->list[Document]:...

def extract_data(path: str, main_key:str="items") -> list[Document]:
    documents: list[Document] = []
    with open(path, "r", encoding='utf8') as json_file:
        data:list[dict[str, str]] = json.load(json_file)[main_key]

        for each_data in data:
            page_content: str = ""
            for k in each_data:
                page_content = page_content + f"{k} {each_data[k]}"
            current_document = Document(
                page_content=page_content,
            )
            documents.append(current_document)
    return documents

# Chunk Splitter
def chunk_splitter(DATA ,WORD_SEPARATOR, CHUNK_SIZE, CHUNK_OVERLAP):
    """
    Function to Split the documents into chunks
    """
    text_splitter = CharacterTextSplitter(separator=WORD_SEPARATOR, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    TEXTS = text_splitter.split_documents(DATA)

    return TEXTS

# Word Embedding 
def word_embedding(TEXTS):
    """
    This part is used for embedding the docs and storing them into VectorDB and initializing the retriever.
    """
    embeddings = OpenAIEmbeddings()
    DOCSEARCH = Chroma.from_documents(TEXTS, embeddings)

    return DOCSEARCH 

# Customize the prompt template for the LLM
def prompt_instruction(PROMPT_INSTRUCTION):
    """
    This part is used for customize the prompt template for the LLM.
    """
    CUSTOM_TEMPLATE = PromptTemplate(
        input_variables=["context", "question"],
        template=PROMPT_INSTRUCTION,
    )

    return CUSTOM_TEMPLATE