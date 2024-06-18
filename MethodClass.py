#MethodClass.py
import os

import google.generativeai as genai
import streamlit as st

from ConstantClass import ConstantClass as cc


class MethodClass:

    # Set google API key
    def set_key():
        genai.configure(api_key = st.secrets.GOOGLE_API_KEY)

    # Create model
    def create_model():
        return genai.GenerativeModel(cc.MODEL_NAME)

    # Process and store Query and Response
    def llm_function(query,model):
        response = model.generate_content(query)


        # Displaying the Assistant Message
        with st.chat_message("assistant"):
            st.markdown(response.text)

        # Storing the User Message
        st.session_state.messages.append(
            {
                "role":"user",
                "content": query
            }
        )

        # Storing the User Message
        st.session_state.messages.append(
            {
                "role":"assistant",
                "content": response.text
            }
        )