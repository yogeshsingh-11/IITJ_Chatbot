from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import os
import pprint
import google.generativeai as palm
from llama_index.embeddings.google import GooglePaLMEmbedding
from llama_index.llms.palm import PaLM
# Create your views here.

def init():
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
        ServiceContext,
        load_index_from_storage
    )
    index = None
    storage_context = StorageContext.from_defaults(persist_dir="D:/IITJ_Chat_Bot_Api/ChatBot/ChatBotApi/storage")
    service_context = ServiceContext.from_defaults(llm=llm, chunk_size=8000, chunk_overlap=20, embed_model=embed_model)
    index= load_index_from_storage(storage_context, service_context=service_context)

    return index

@api_view(['POST'])
def getbotresponse(request):
    index = init()
    if request.method == 'POST':
        query = request.body.decode('utf-8')
        # query = "where is RAPS located ?"
        # print("Checking")
        query_engine = index.as_query_engine()
        response = query_engine.query(query)
        response = str(response)
        return Response({'result': response}, status = status.HTTP_200_OK)
    else:
        return Response({'Error': 'We only use post requests'}, status = status.HTTP_400_BAD_REQUEST)
