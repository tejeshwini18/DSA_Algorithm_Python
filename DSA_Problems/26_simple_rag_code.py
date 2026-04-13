from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# 1. Load documents
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

# 3. Create embeddings
embeddings = OpenAIEmbeddings()

# 4. Store in vector DB
vectorstore = FAISS.from_documents(docs, embeddings)

# 5. Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 6. Create LLM
llm = ChatOpenAI(model="gpt-4o-mini")  # cheaper & recommended

# 7. Create RAG chain
qa = RetrievalQA.from_chain_type(
    llm=llm, 
    retriever=retriever
)

# 8. Query
response = qa.invoke({"query": "What is the main topic?"})
print(response["result"])