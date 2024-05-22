import os
from flask import request
# from llama_index.llms.gemini import Gemini
import pprint
import google.generativeai as palm
# imports
from llama_index.embeddings.google import GooglePaLMEmbedding
from llama_index.llms.palm import PaLM
# from llama_index import ServiceContext

model_name = "models/embedding-gecko-001"
api_key = "AIzaSyB82ecM2-7I0EEGMz1uhOzCosYP0BQwvKk"

palm_api_key = "AIzaSyB82ecM2-7I0EEGMz1uhOzCosYP0BQwvKk"
palm.configure(api_key=palm_api_key)


embed_model = GooglePaLMEmbedding(model_name=model_name, api_key=api_key)


llm = PaLM(api_key=palm_api_key)
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    ServiceContext
)



index = None

service_context = ServiceContext.from_defaults(llm=llm, chunk_size=8000, chunk_overlap=20, embed_model=embed_model)
documents = SimpleDirectoryReader("D:/IITJ_Chat_Bot_Api/ChatBot/ChatBotApi/documents").load_data()
index = VectorStoreIndex.from_documents(
            documents,service_context=service_context
        )
index.storage_context.persist(persist_dir="D:/IITJ_Chat_Bot_Api/ChatBot/ChatBotApi/storage")
