from langchain.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA

# Initialize Chroma DB and OpenAI embeddings
embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
chroma_db = Chroma(persist_directory="./chroma_data", embedding_function=embedding_function)

# Add documents to the Chroma database (if empty)
if not chroma_db.get().ids:
    documents = [
        {"id": "1", "text": "The capital of France is Paris."},
        {"id": "2", "text": "Python is a versatile programming language."},
    ]
    for doc in documents:
        chroma_db.add_texts([doc["text"]])

# Setup LangChain RetrievalQA
#llm = OpenAI(openai_api_key="your-gemini-or-openai-api-key", temperature=0)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=chroma_db.as_retriever())

def ask_question(question: str) -> str:
    """Process the user's question using RAG."""
    try:
        response = qa_chain.run(question)
        return response
    except Exception as e:
        return f"Error: {e}"
