import openai
import streamlit as st
import time
import os
import zipfile
import yaml
 
from inference_assistant import inference
from utils import create_assistant_from_config_file, upload_to_openai, export_assistant

st.set_page_config(
    page_title="Pilot",
    page_icon="🤖",
    layout="wide",
    menu_items={
        'Get Help': 'mailto:lancos@datawhisper.co.uk',
        'About': "# This is  API\n\n"
    }
)

st.title("Glidding technical assistant !")
##st.caption (" Welcome to the Gliding Technical Knowledge Bot, your specialized assistant for all things related to gliding")
##st.caption (" Just say hello and Hi and I will let you know what I can do for you." )




openaiKey = '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'
id_assistente = 'asst_axrsu71yTNAXbzyf1Nv1EJ59'

if openaiKey:
    os.environ["OPENAI_API_KEY"] = openaiKey
    openai.api_key = openaiKey
    client = openai.OpenAI()


# Inferenza con Assistente

if id_assistente:
    try: 
        inference(id_assistente)
    except Exception as e:
        st.error("🛑 There was a problem with OpenAI Servers")
        st.error(e)
        if st.button("🔄 Restart"):
            st.rerun()

html_chat = '<center><h6></h6>'
st.markdown(html_chat, unsafe_allow_html=True)
st.write('Made with ❤️ by [Luis Lancos, Essex Gliding club](https://datawhisper.co.uk)')