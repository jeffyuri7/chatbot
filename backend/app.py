#!/usr/bin/env python3
import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8502/chatbot")


# Função para gerar resposta do bot usando OpenAI GPT
def generate_bot_response(user_input):
    try:
        return remote_chain.invoke({"texto": user_input})
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"


# Função para adicionar a interação de input do usuário e resposta do bot
def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)  # Armazena a pergunta do usuário

    # Gerar resposta do bot (pode ser modificado para qualquer lógica)
    bot_response = generate_bot_response(user_input)
    st.session_state.generated.append({"type": "normal", "data": bot_response})

    # Limpar o campo de entrada de texto após a interação
    st.session_state.user_input = ""


# Função para limpar o histórico de conversas
def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


# Inicializar o estado da sessão, com exemplos prévios
st.session_state.setdefault("past", [])
st.session_state.setdefault("generated", [])

st.set_page_config(page_title="Chatbot - WAProject", page_icon="robot_face")
st.title("Chatbot Interativo")
st.subheader("Desafio WAProject - Python Aprendizado Contínuo")

chat_placeholder = st.empty()

# Exibição das mensagens do usuário e respostas do bot
with chat_placeholder.container():
    for i in range(len(st.session_state["generated"])):
        message(st.session_state["past"][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state["generated"][i]["data"],
            key=f"{i}_bot",
            allow_html=True,
            is_table=(
                True if "table" in st.session_state["generated"][i]["type"] else False
            ),
        )

    st.button("Limpar Mensagens", on_click=on_btn_click)

# Área de entrada de texto do usuário
with st.container():
    mensagem = st.text_input(
        "Digite sua mensagem:", on_change=on_input_change, key="user_input"
    )
