from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from chat_rag.embedding import embeddings

parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=50)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)

vector_store = Chroma(
    collection_name="document",
    embedding_function=embeddings,
    # persist_directory="../chroma_db"
)

store = InMemoryStore()

retriever = ParentDocumentRetriever(
    vectorstore=vector_store,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)
