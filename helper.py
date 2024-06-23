from langchain_community.llms import GooglePalm
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.csv_loader import CSVLoader
import google.generativeai as palm
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA


vectordb_file_path = "faiss_index"

load_dotenv()
api_key=os.environ["GOOGLE_API_KEY"]
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)


embeddings = HuggingFaceEmbeddings()
def create_db():
    loader=CSVLoader(file_path="data.csv", source_column="prompt")
    data=loader.load()
    db = FAISS.from_documents(data, embeddings) 
    db.save_local(vectordb_file_path)
def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, embeddings,allow_dangerous_deserialization=True)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain

if __name__ == "__main__":
    create_db()
    chain = get_qa_chain()
    print(chain("Do you have javascript course?"))
    