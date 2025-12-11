import os
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA


load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")

@st.cache_resource
def load_pdf_and_create_chain(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(docs)

    embeddings = MistralAIEmbeddings(model="mistral-embed", mistral_api_key=mistral_api_key)
    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatMistralAI(
        model="mistral-large-latest",
        temperature=0.6,
        mistral_api_key=mistral_api_key
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain


st.set_page_config(page_title="Agentic AI", layout="centered")
st.title("Agentic AI")

pdf_path = "Ebook-Agentic-AI.pdf"
qa_chain = load_pdf_and_create_chain(pdf_path)


user_question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if user_question.strip():
        with st.spinner("Analyzing... Please wait."):
            result = qa_chain.invoke(user_question)
        
        st.subheader("Answer:")
        st.write(result["result"])

        with st.expander("View Sources"):
            for idx, doc in enumerate(result["source_documents"], 1):
                st.write(f"**Source {idx}:** {doc.metadata.get('source', 'Unknown')}")
                st.write(doc.page_content[:300] + "...")
    else:
        st.warning("Please enter a question.")
