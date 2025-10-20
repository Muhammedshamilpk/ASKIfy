# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory
# from .llm_handler import LLMHandler
# from document_handler import DocumentHandler

# class ChatManager:
#     """Manages RAG flow and chat memory."""
#     def __init__(self):
#         self.llm_handler = LLMHandler()
#         self.document_handler = DocumentHandler()
#         self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#         self.vector_store = self.document_handler.build_vector_store()
#         self.chain = self._create_chain() if self.vector_store else None

#     def _create_chain(self):
#         return ConversationalRetrievalChain.from_llm(
#             llm=self.llm_handler.get_model(),
#             retriever=self.vector_store.as_retriever(),
#             memory=self.memory
#         )

#     def is_ready(self):
#         return self.chain is not None

#     def get_response(self, user_input):
#         return self.chain({"question": user_input})




# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory
# from .llm_handler import LLMHandler
# from .document_handler import DocumentHandler

# class ChatManager:
#     """Manages RAG flow and chat memory."""
#     def __init__(self):
#         self.llm_handler = LLMHandler()
#         self.document_handler = DocumentHandler()
#         self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#         self.vector_store = self.document_handler.build_vector_store()
#         self.chain = self._create_chain() if self.vector_store else None

#     def _create_chain(self):
#         return ConversationalRetrievalChain.from_llm(
#             llm=self.llm_handler.get_model(),
#             retriever=self.vector_store.as_retriever(),
#             memory=self.memory
#         )

#     def is_ready(self):
#         return self.chain is not None

#     def get_response(self, user_input):
#         return self.chain({"question": user_input})





# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory

# class ChatManager:
#     """Manages RAG flow and chat memory."""

#     def __init__(self, document_handler, llm_handler):
#         self.llm_handler = llm_handler
#         self.document_handler = document_handler
#         self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#         self.vector_store = self.document_handler.build_vector_store()
#         self.chain = self._create_chain() if self.vector_store else None
#         self.last_retrieved_sources = []

#     def _create_chain(self):
#         return ConversationalRetrievalChain.from_llm(
#             llm=self.llm_handler.get_model(),
#             retriever=self.vector_store.as_retriever(),
#             memory=self.memory
#         )

#     def is_ready(self):
#         return self.chain is not None

#     def ask(self, user_input, chat_history=[]):
#         if not self.is_ready():
#             return "No documents loaded.", []

#         result = self.chain({"question": user_input})
#         # Save sources for optional display
#         self.last_retrieved_sources = result.get("source_documents", [])
#         return result.get("answer", "No answer found."), self.last_retrieved_sources







from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

class ChatManager:
    """Manages RAG flow and chat memory."""
    def __init__(self, document_handler, llm_handler):
        self.document_handler = document_handler
        self.llm_handler = llm_handler
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Build chain if vector store exists
        self.vector_store = getattr(self.document_handler, "vector_store", None)
        self.chain = self._create_chain() if self.vector_store else None
        self.last_retrieved_sources = []

    def _create_chain(self):
        return ConversationalRetrievalChain.from_llm(
            llm=self.llm_handler.get_model(),
            retriever=self.vector_store.as_retriever(),
            memory=self.memory
        )

    def is_ready(self):
        return self.chain is not None

    def get_response(self, user_input):
        if not self.chain:
            return {"answer": "No documents loaded."}
        result = self.chain({"question": user_input})
        self.last_retrieved_sources = result.get("source_documents", [])
        return result
