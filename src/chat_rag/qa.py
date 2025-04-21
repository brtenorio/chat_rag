from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from chat_rag.chat_model import LLMmodel
from chat_rag.retriever import retriever


class QA:
    def __init__(self, model=None, max_num_tokens=None):
        self.model = model
        self.max_num_tokens = int(max_num_tokens)

    def load(self):
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_message=True
        )
        llm = LLMmodel(self.model, self.max_num_tokens).load()

        return ConversationalRetrievalChain.from_llm(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=False,
            memory=memory,
            get_chat_history=lambda h: h,
        )
