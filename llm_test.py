# Import relevant libraries
import os
from dotenv import load_dotenv
import openai
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()

try:
    # Set api_key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Load documents from the directory and create an index on them
    documents = SimpleDirectoryReader("C:\\Users\\ved\\falcon\\llm\\data").load_data()
    index = VectorStoreIndex.from_documents(documents)

    # Question to ask the LLM
    question = input("Ask a question about the documents: ")

    while question.lower() != "quit":
        # Return and display the response
        response = index.as_query_engine()
        print(response.query(question))
        question = input("Ask a question about the documents: ")


except Exception as e:
    print("Error : ", e)


