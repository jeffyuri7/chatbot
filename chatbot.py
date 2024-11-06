#!/usr/bin/env python3
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
model = ChatGroq(model="llama3-8b-8192")
parser = StrOutputParser()

template_mensagem = ChatPromptTemplate(
    [("system", "Traduza o texto para o idioma {idioma}"), ("user", "{texto}")]
)

chain = template_mensagem | model | parser

texto = chain.invoke({"idioma": "francês", "texto": "Eu sou bonito"})
print(texto)
