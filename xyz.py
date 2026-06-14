from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:\\Users\\sy505\\OneDrive\\Desktop\\my_project\\1706.03762v7.pdf")
docs = loader.load()
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100,separator="/n"))
text = splitter.split()
from langchain.embeddings import Embeddings
from langchain_classic.vectorstores import FAISS
embad = Embeddings("Sentence transformer"")
vector = FAISS.from(embad,text)
from langchain_classic.retrievers import EnsembleRetriever
from langchain_classic.retrievers import BM25Retriever
retriever = vector_store.as retriever(search type = "cosine similarity",kwargs:3)
from langchain_classic.chat_models import init_chat_model
from langchain_classic.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

response = llm.invoke("What is semantic search?")
print(response)




