
    

    
import streamlit as st
from .config import Config
# Gemini imports
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ModuleNotFoundError:
    ChatGoogleGenerativeAI = None

# HuggingFace imports
try:
    from langchain_huggingface import HuggingFaceEndpoint
except ModuleNotFoundError:
    HuggingFaceEndpoint = None

class LLMHandler:
    """Initializes Gemini or Hugging Face model."""
    def __init__(self):
        self.config = Config()
        self.model = self._initialize_model()

    def _initialize_model(self):
        try:
            if self.config.model_provider == "gemini":
                if ChatGoogleGenerativeAI is None:
                    st.error("Gemini module not installed.")
                    st.stop()
                return ChatGoogleGenerativeAI(
                    model="gemini-2.0-flash",
                    google_api_key=self.config.gemini_key
                )
            else:
                if HuggingFaceEndpoint is None:
                    st.error("HuggingFace module not installed.")
                    st.stop()
                return HuggingFaceEndpoint(
                    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
                    huggingfacehub_api_token=self.config.hf_token
                )
        except Exception as e:
            st.error(f"Failed to initialize model: {str(e)}")
            st.stop()

    def get_model(self):
        return self.model



