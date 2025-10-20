

# import streamlit as st
# from chatbot.document_handler import DocumentHandler
# from chatbot.llm_handler import LLMHandler
# from chatbot.chat_manager import ChatManager

# st.set_page_config(page_title=" ASKIfy AI", layout="wide")

# # Initialize handlers
# doc_handler = DocumentHandler("docs")
# llm_handler = LLMHandler()
# chat_manager = ChatManager(doc_handler, llm_handler)

# # Session state for chat history
# if "history" not in st.session_state:
#     st.session_state.history = []

# # Sidebar: upload documents
# st.sidebar.header("📤 Upload / Index Documents")
# uploaded_files = st.sidebar.file_uploader(
#     "Upload TXT or PDF files", type=["txt", "pdf"], accept_multiple_files=True
# )

# if uploaded_files:
#     with st.spinner("Processing uploaded files..."):
#         for f in uploaded_files:
#             ext = f.name.lower().split(".")[-1]
#             if ext == "pdf":
#                 text = doc_handler._extract_text_from_pdf_stream(f)
#             else:
#                 text = f.read().decode("utf-8")
#             doc_handler.add_document_text(f.name, text)
#         doc_handler.build_faiss()
#     st.sidebar.success(f"{len(uploaded_files)} file(s) indexed!")
#     chat_manager = ChatManager(doc_handler, llm_handler)  # refresh chain

# # Rebuild FAISS from docs folder
# if st.sidebar.button("Rebuild FAISS from docs/ folder"):
#     with st.spinner("Building FAISS index..."):
#         doc_handler.build_faiss()
#     st.sidebar.success("FAISS index rebuilt successfully!")
#     chat_manager = ChatManager(doc_handler, llm_handler)  # refresh chain

# # Main chat
# st.title("📚 ASKIfy AI")
# st.subheader("Ask questions about your documents 💬")

# query = st.chat_input("Type your question here...")
# if query:
#     st.session_state.history.append(("user", query))
#     with st.spinner("Generating response..."):
#         response = chat_manager.get_response(query)
#         answer = response.get("answer", "No answer found.")
#         st.session_state.history.append(("assistant", answer))

# # Render chat messages
# for role, text in st.session_state.history:
#     st.chat_message(role).write(text)

# # Show last retrieved sources
# if st.sidebar.checkbox("Show last retrieved sources") and chat_manager.is_ready():
#     st.sidebar.markdown("### 📄 Top Retrieved Documents")
#     for i, doc in enumerate(chat_manager.last_retrieved_sources):
#         page_content = getattr(doc, "page_content", "")
#         metadata = getattr(doc, "metadata", {})
#         source_name = metadata.get("source", f"doc_{i}")
#         st.sidebar.markdown(f"**{i+1}. {source_name}**")
#         st.sidebar.write(page_content[:400] + ("..." if len(page_content) > 400 else ""))



import streamlit as st
from chatbot.document_handler import DocumentHandler
from chatbot.llm_handler import LLMHandler
from chatbot.chat_manager import ChatManager

st.set_page_config(page_title="📚 ASKIfy AI", layout="wide")

# -------------------------
# Initialize handlers
# -------------------------
doc_handler = DocumentHandler("docs")
llm_handler = LLMHandler()
chat_manager = ChatManager(doc_handler, llm_handler)

# -------------------------
# Session state
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# Layout: Two Columns
# -------------------------
chat_col, sidebar_col = st.columns([3, 1])

with sidebar_col:
    st.header("⚙️ Controls")
    
    # Upload files
    uploaded_files = st.file_uploader(
        "Upload TXT or PDF", type=["txt", "pdf"], accept_multiple_files=True
    )
    if uploaded_files:
        st.info(f"Processing {len(uploaded_files)} file(s)...")
        with st.spinner("Indexing documents..."):
            for f in uploaded_files:
                ext = f.name.lower().split(".")[-1]
                text = doc_handler._extract_text_from_pdf_stream(f) if ext == "pdf" else f.read().decode("utf-8")
                doc_handler.add_document_text(f.name, text)
            doc_handler.build_faiss()
        st.success(f"{len(uploaded_files)} file(s) indexed!")
        chat_manager = ChatManager(doc_handler, llm_handler)  # refresh chain

    # Rebuild FAISS
    if st.button("🔄 Rebuild FAISS from docs folder"):
        with st.spinner("Rebuilding FAISS index..."):
            doc_handler.build_faiss()
        st.success("FAISS index rebuilt successfully!")
        chat_manager = ChatManager(doc_handler, llm_handler)

    # Clear chat
    if st.button("🧹 Clear Chat"):
        st.session_state.history = []

    # Retrieved sources
    if st.checkbox("📄 Show retrieved sources") and chat_manager.is_ready():
        st.markdown("### Retrieved Documents")
        for i, doc in enumerate(chat_manager.last_retrieved_sources):
            page_content = getattr(doc, "page_content", "")
            metadata = getattr(doc, "metadata", {})
            source_name = metadata.get("source", f"doc_{i}")
            with st.expander(f"{i+1}. {source_name}"):
                st.write(page_content[:500] + ("..." if len(page_content) > 500 else ""))

# -------------------------
# Chat Area
# -------------------------
with chat_col:
    st.title("🌐 ASKfy.ai")
    st.subheader("Turn your file into friendly chat ! 🧑‍💻")

    query = st.chat_input("Type your question here...")
    if query:
        st.session_state.history.append(("user", query))
        with st.spinner("Generating response..."):
            response = chat_manager.get_response(query)
            answer = response.get("answer", "No answer found.")
            st.session_state.history.append(("assistant", answer))

    # Display messages
    for role, text in st.session_state.history:
        if role == "user":
            st.chat_message("user", avatar="🧑").markdown(f"**{text}**")
        else:
            st.chat_message("assistant", avatar="🤖").markdown(text)
