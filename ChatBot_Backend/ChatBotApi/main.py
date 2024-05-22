import os
import pprint
import google.generativeai as palm
from llama_index.embeddings.google import GooglePaLMEmbedding
from llama_index.llms.palm import PaLM
load_dotenv()

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
storage_context = StorageContext.from_defaults(persist_dir="./storage")
service_context = ServiceContext.from_defaults(llm=llm, chunk_size=8000, chunk_overlap=20, embed_model=embed_model)
index= load_index_from_storage(storage_context, service_context=service_context)

def answer(query):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response



# @app.route("/")
# def home():
#     return render_template('index.html')

# @app.route("/query", methods=["GET"])
# def query_index():
#     global index
#     query_text = request.args.get("text", None)
#     if query_text is None:
#         return (
#             "No text found, please include a ?text=blah parameter in the URL",
#             400,
#         )

    
#     query_engine = index.as_query_engine()
#     response = query_engine.query(query_text)

#     response_json = {
#         "text": str(response)
#     }
#     return make_response(jsonify(response_json)), 200
   