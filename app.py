import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Constants
DB_NAME = "vectorstore"
MAX_FILE_SIZE = 200 * 1024 * 1024  # 200MB limit

# Streamlit UI setup
st.title("AI-Powered QnA Assistant")

# File Upload Section
uploaded_file = st.file_uploader("Upload a .pdf or .docx file (Max: 200MB)", type=["pdf", "docx"])

# Define loader function
def get_loader(file_path):
    if file_path.endswith('.pdf'):
        return PyPDFLoader(file_path)
    elif file_path.endswith('.docx'):
        return Docx2txtLoader(file_path)
    else:
        raise RuntimeError("Unsupported file format")

# Process the uploaded file
if uploaded_file:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("❌ File exceeds the 200MB size limit. Please upload a smaller file.")
    else:
        # Save file temporarily in the 'knowledge-base' folder
        knowledge_base_dir = "knowledge-base"
        os.makedirs(knowledge_base_dir, exist_ok=True)

        file_path = os.path.join(knowledge_base_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

        # Load and process document
        try:
            loader = get_loader(file_path)
            documents = loader.load()
        except Exception as e:
            st.error(f"❌ Error loading document: {e}")
            documents = []

        if documents:
            # Split documents into chunks for vector storage
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_documents(documents)

            # Create embeddings
            embeddings = OpenAIEmbeddings()

            # Delete existing vector database if present
            if os.path.exists(DB_NAME):
                Chroma(persist_directory=DB_NAME, embedding_function=embeddings).delete_collection()

            # Create new vector store
            vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=DB_NAME)

            # Store vectorstore in session state for persistent access
            st.session_state.vectorstore = vectorstore
            st.success("✅ Document processed and ready for QnA!")

# Chat Section (Independent of file upload logic)
if "vectorstore" in st.session_state:
    st.header("Ask Questions Based on Uploaded Document")
    user_question = st.text_area("Enter your question here:")

    if st.button("Start Chat"):
        if user_question.strip():
            # Initialize model and memory
            llm = ChatOpenAI(temperature=0.7)
            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
            retriever = st.session_state.vectorstore.as_retriever()

            # Conversation chain setup
            conversation_chain = ConversationalRetrievalChain.from_llm(
                llm=llm, retriever=retriever, memory=memory
            )

            # Process user question
            result = conversation_chain.invoke({"question": user_question})
            answer = result["answer"][:1000]  # Limit response to 1000 words
            st.markdown(f"**Answer:** {answer}")
        else:
            st.warning("⚠️ Please enter a question before clicking 'Start Chat'.")
