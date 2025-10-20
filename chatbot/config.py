
         
         

import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

class Config:
    """
    Configuration class for managing API keys and model selection.
    Supports Gemini (Google) and Hugging Face providers.
    """

    def __init__(self):
        # === Model Provider ===
        # Choose between: "gemini" or "huggingface"
        self.model_provider = os.getenv("MODEL_PROVIDER", "gemini").lower()

        # === Gemini Configuration ===
        self.gemini_key = os.getenv("GEMINI_API_KEY", "")
        self.model_name = os.getenv("GEMINI_MODEL_NAME", "gemini-2.0-flash")

        # === Hugging Face Configuration ===
        self.hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN", "")
        self.repo_id = os.getenv("HF_REPO_ID", "mistralai/Mistral-7B-Instruct-v0.3")

        # === Validation ===
        self._validate_keys()

    def _validate_keys(self):
        """Validate that required API keys are set for the selected provider."""
        if self.model_provider == "gemini" and not self.gemini_key:
            st.error("❌ Gemini API key missing. Please set GEMINI_API_KEY in your environment or .env file.")
            st.stop()

        elif self.model_provider == "huggingface" and not self.hf_token:
            st.error("❌ Hugging Face token missing. Please set HUGGINGFACEHUB_API_TOKEN in your environment or .env file.")
            st.stop()
