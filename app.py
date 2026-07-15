import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from persona_compadre import SYSTEM_PROMPT as COMPADRE_PROMPT
from persona_cariani import SYSTEM_PROMPT as CARIANI_PROMPT
from persona_maicon import SYSTEM_PROMPT as MAICON_PROMPT
from persona_manoel import SYSTEM_PROMPT as MANOEL_PROMPT

load_dotenv()

MODEL = "llama-3.3-70b-versatile"

PERSONAS = {
    "🧔🏿‍♂️ Compadrebot": {
        "prompt": COMPADRE_PROMPT,
        "title": "Compadrebot",
        "icon": "🧔🏿‍♂️",
        "caption": "O chatbot mais arretado da internet, meu rei!",
        "placeholder": "Manda a pergunta, sô...",
    },
    "🧤 Maicon Jéquebot": {
        "prompt": MAICON_PROMPT,
        "title": "Maicon Jéquebot",
        "icon": "🧤",
        "caption": "O sósia cearense do Michael Jackson, Xamone!!",
        "placeholder": "Pergunta aí, caboco...",
    },
    "💪 Cariribot": {
        "prompt": CARIANI_PROMPT,
        "title": "Cariribot",
        "icon": "💪",
        "caption": "Eu quero, eu posso!",
        "placeholder": "Manda a pergunta, Ramon...",
    },
    "🎸 Manoelbot": {
        "prompt": MANOEL_PROMPT,
        "title": "Manoelbot",
        "icon": "🎸",
        "caption": "Portugueizi bom demaize",
        "placeholder": "Pergunta aí, meu chegado...",
    },
}

st.set_page_config(page_title="Compadrebot", page_icon="🧔🏿‍♂️")

with st.sidebar:
    st.header("Persona")
    selected_persona = st.radio(
        "Escolha com quem falar:",
        options=list(PERSONAS.keys()),
        key="selected_persona",
    )

persona = PERSONAS[selected_persona]

st.title(f"{persona['icon']} {persona['title']}")
st.caption(persona["caption"])

api_key = os.environ.get("GROQ_API_KEY") or sk_D6LuoakAzWW5dOQuixmiWGdyb3FYbOfXD0c1R2dlrPzmMCMoA4Dc 

if not api_key:
    st.warning(
        "Oxente, cumpadi! Cadê a chave da API? Crie um arquivo `.env` na "
        "raiz do projeto com `GROQ_API_KEY=sua_chave_aqui` e reinicie o app."
    )
    st.stop()

client = Groq(api_key=api_key)

history_key = f"messages_{selected_persona}"

if history_key not in st.session_state:
    st.session_state[history_key] = [
        {"role": "system", "content": persona["prompt"]}
    ]

for message in st.session_state[history_key]:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input(persona["placeholder"])

if user_input:
    st.session_state[history_key].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state[history_key],
            stream=True,
        )

        def token_stream():
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    yield delta

        response = st.write_stream(token_stream)

    st.session_state[history_key].append({"role": "assistant", "content": response})
