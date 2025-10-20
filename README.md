# 🧠 ASKfy -Turn your file into friendly chat ! 🧑‍💻
Using gemini, Hugging Face, FAISS, and LangChain
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🎯 Project Objective

This project is a Streamlit-based AI chatbot that allows users to chat with their uploaded documents (PDF or TXT).


It integrates LangChain, FAISS, and LLMs (groq or Hugging Face) to provide contextual, intelligent answers based on document content.



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 🧩 Core Learning Goals

▪By completing this project, you will learn to:

▪Integrate LangChain for Retrieval-Augmented Generation (RAG)

▪Use Groq or Hugging Face models for conversational AI

▪Implement FAISS for efficient semantic retrieval

▪Apply OOP principles to modularize chatbot logic

▪Build and deploy an interactive Streamlit web interface

▪Create professional software documentation and diagrams


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ⚙ Tech Stack

| Category                   | Technology                                                               |
| -------------------------- | ------------------------------------------------------------------------ |
| *Frontend (UI)*          | Streamlit                                                                |
| *Backend Framework*      | LangChain                                                                |
| *LLMs*                   | GEMINI_MODEL=gemini-2.0-flash /Hugging Face (Mistral-7B-Instruct-v0.3) |
| *Vector Database*        | FAISS                                                                    |
| *Embedding Model*        | GEMINI / Hugging Face Embeddings (EMBEDDING_MODEL=all-MiniLM-L6-v2)                                     |
| *Language*               | Python 3.10+                                                             |
| *Environment Management* | .env + python-dotenv                                                 |
| *Version Control*        | Git & GitHub                                                             |
| *Documentation*          | Markdown + Diagrams (Mermaid / draw.io)                                  |




------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📁 Project Structure



Doc-Chat/
│

├── app.py                     # Main Streamlit app (entry point)

│

├── chatbot/

│   ├── _init_.py

│   ├── config.py              # Loads & validates environment variables

│   ├── llm_handler.py         # Initializes Gemini/Hugging Face models

│   ├── document_handler.py    # Handles document loading and FAISS setup

│   ├── chat_manager.py        # Manages conversation & retrieval chain

│   └── utils.py               # Optional helper functions

│

├── .env                       # API keys and provider name

├── requirements.txt

└── README.md


--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ⚙ 1. Setup & Configuration


🔹 Step 1: Install Dependencies

-->pip install -r requirements.txt



🔹 Step 2: Create .env File


-->MODEL_PROVIDER=groq     # or huggingface
-->GEMINI_API_KEY=your_gemini_key



🔹 Step 3: Run the App

-->streamlit run app.py


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 🧱 2. Class Overview (OOP Modules)


🧩 Config (config.py)

Loads environment variables with dotenv

Validates model provider and API keys

Raises exceptions for invalid configuration


🧩 LLMHandler (llm_handler.py)

Initializes Gemini or Hugging Face models

Handles API errors and connection issues

Uses modular OOP design for easy extension


🧩 DocumentHandler (document_handler.py)

Loads and processes PDF/TXT documents

Splits text using RecursiveCharacterTextSplitter

Generates embeddings and builds FAISS vector store


🧩 ChatManager (chat_manager.py)

Uses ConversationalRetrievalChain from LangChain

Maintains chat history with ConversationBufferMemory

Retrieves context and generates responses


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 💬 3. Streamlit Frontend (app.py)

Provides a clean and interactive chat interface

Uses st.chat_message() for chat bubbles

Supports uploading .pdf and .txt files

Displays model responses and friendly error messages

Maintains chat history in st.session_state


------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🧱 4. OOP & Modular Programming Concepts


| Principle          | Description                           |
| ------------------ | ------------------------------------- |
| *Encapsulation*  | Each class handles one responsibility |
| *Abstraction*    | Complex logic hidden in clean methods |
| *Inheritance*    | Optional for extending chatbot logic  |
| *Error Handling* | Meaningful exceptions with try/except |


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🧭 5. Workflow Diagram


<img width="647" height="1346" alt="Mermaid Chart - Create complex, visual diagrams with text -2025-10-20-090420" src="https://github.com/user-attachments/assets/fd0d0f82-b107-4331-91c3-9da6e155e16c" />



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Architeture Digram

<img width="584" height="586" alt="Mermaid Chart - Create complex, visual diagrams with text -2025-10-20-090549" src="https://github.com/user-attachments/assets/4c16323d-7e8d-4c57-ba42-a1d33a2111b1" />




-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 7. SEQUENCE Diagram


<img width="2120" height="978" alt="Mermaid Chart - Create complex, visual diagrams with text -2025-10-20-090901" src="https://github.com/user-attachments/assets/4fb8a3ac-df95-4516-8f0c-598e90e81907" />





----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8.Class diagram


<img width="1037" height="1108" alt="Mermaid Chart - Create complex, visual diagrams with text -2025-10-20-090622" src="https://github.com/user-attachments/assets/b4183392-05e3-486f-8498-3023f7bac7fd" />



----------------------------------------------------------------------------------------------------------------------------------------------------------------



# 🧾 9. Git Workflow

git add .
git commit -m "feat: add LLMHandler with Gemini and Hugging Face support"
git push origin main

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ✔ output


<img width="1848" height="952" alt="Screenshot 2025-10-20 151108" src="https://github.com/user-attachments/assets/819e7ea0-7afc-47b7-bf26-ebfa7e868727" />



<img width="1856" height="973" alt="Screenshot 2025-10-20 151357" src="https://github.com/user-attachments/assets/8725faa1-2b48-4bff-8d31-17fd79126062" />










------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Author:MUHAMMED SHAMIL P K
