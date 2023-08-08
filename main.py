"""
Streamlit file
Autor: LuizoMatias
"""
import streamlit as st
from src.voice_clone import VoiceGenerator
from src.langchain_chatgpt import chatgpt_result


st.header("Robot With Your Cloned Voice!")

system_prompt = st.text_input(
    "Robot Personality", placeholder="Write the robot's personality..."
)

human_prompt = st.text_input(
    "Envie uma mensagem", placeholder="Write your prompt here..."
)

option_language = st.selectbox("Which language?", ("English", "Portuguese"))

button = st.button("Run")

if human_prompt and system_prompt:
    if button:
        with st.spinner("Generating response..."):
            voice = VoiceGenerator("my_voice")

            chat_content = chatgpt_result(system_prompt, human_prompt)

            audio_file = voice.text_to_speech(option_language, chat_content)

            message = st.chat_message("assistant")

            message.write("I'm the robot with your voice!")

            st.audio(audio_file)
