# https://blog.futuresmart.ai/building-a-conversational-voice-chatbot-integrating-openais-speech-to-text-text-to-speech
# Reference: See above

import streamlit as st
import hmac
# import argparse

import os
from helpers import text_to_speech, autoplay_audio, speech_to_text
from generate_answer import base_model_chatbot, with_pdf_chatbot
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *

def main(answer_mode: str):
    # Float feature initialization
    float_init()


    def check_password():
        """Returns `True` if the user had a correct password."""

        def login_form():
            """Form with widgets to collect user information"""
            with st.form("Credentials"):
                st.text_input("Username", key="username")
                st.text_input("Password", type="password", key="password")
                st.form_submit_button("Log in", on_click=password_entered)

        def password_entered():
            """Checks whether a password entered by the user is correct."""
            if st.session_state["username"] in st.secrets[
                "passwords"
            ] and hmac.compare_digest(
                st.session_state["password"],
                st.secrets.passwords[st.session_state["username"]],
            ):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  
                del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False

        # Return True if the username + password is validated.
        if st.session_state.get("password_correct", False):
            return True

        # Show inputs for username + password.
        login_form()
        if "password_correct" in st.session_state:
            st.error("😕 User not known or password incorrect")
        return False


    if not check_password():
        st.stop()


    def initialize_session_state():
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi! How may I assist you today?"}
            ]


    initialize_session_state()

    st.title("OpenAI Conversational Chatbot 🤖")

    # Create footer container for the microphone
    footer_container = st.container()
    with footer_container:
        audio_bytes = audio_recorder()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if audio_bytes:
        # Write the audio bytes to a file
        with st.spinner("Transcribing..."):
            webm_file_path = "temp_audio.mp3"
            with open(webm_file_path, "wb") as f:
                f.write(audio_bytes)

            transcript = speech_to_text(webm_file_path)
            if transcript:
                st.session_state.messages.append({"role": "user", "content": transcript})
                with st.chat_message("user"):
                    st.write(transcript)
                os.remove(webm_file_path)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking🤔..."):
                if answer_mode == 'base_model':
                    final_response = base_model_chatbot(st.session_state.messages)
                elif answer_mode == 'pdf_chat':
                    print('--------->', st.session_state.messages)
                    final_response = with_pdf_chatbot(st.session_state.messages)
            with st.spinner("Generating audio response..."):
                audio_file = text_to_speech(final_response)
                autoplay_audio(audio_file)
            st.write(final_response)
            st.session_state.messages.append({"role": "assistant", "content": final_response})
            os.remove(audio_file)

    # Float the footer container and provide CSS to target it with
    footer_container.float("bottom: 0rem;")
 
if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Run OpenAI Conversational Chatbot")
    # parser.add_argument('--answer_mode', type=str, default='base_model',
    #                     choices=['base_model', 'pdf_chat'],
    #                     help="Specify the answer mode ('base_model' or 'pdf_chat')")

    # args = parser.parse_args()

    main(answer_mode='base_model') # Or: answer_mode='base_model'