#!/usr/bin/env python3
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import chromadb

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar o modelo de linguagem (ChatGroq)
model = ChatGroq(model="llama3-8b-8192")
parser = StrOutputParser()

# Configurar o template do prompt para o chatbot
template_mensagem = ChatPromptTemplate(
    [("system", "Você é um assistente de ajuda médica"), ("user", "{texto}")]
)

# Montar a cadeia de execução do chatbot (modelo + parser)
chain = template_mensagem | model | parser

# Conectar ao Chroma (banco de dados vetorial)
client = chromadb.HttpClient(host="chroma-db", port=8000)
client.heartbeat()
# collection = client.create_collection("user_data")


# Função para armazenar dados no Chroma (vetorizar o texto)
def store_vector_in_db(text: str):
    # Gerar o embedding (vetor) do texto
    vector = embedding.embed_query(text)

    # Adicionar o texto e o embedding ao banco de dados Chroma
    collection.add(
        documents=[text], metadatas=[{"source": "user_input"}], embeddings=[vector]
    )


# Função para buscar dados semelhantes no Chroma
def retrieve_from_db(query: str):
    # Gerar o embedding da query do usuário
    vector = embedding.embed_query(query)

    # Buscar os documentos mais semelhantes no Chroma
    results = collection.query(
        query_embeddings=[vector], n_results=3  # Número de resultados mais próximos
    )

    return results["documents"]


# Função principal que processa a entrada do usuário
def process_user_input(texto: str):
    # Armazenar a entrada do usuário no banco de dados vetorial (Chroma)
    store_vector_in_db(texto)

    # Recuperar documentos semelhantes ao texto do usuário
    similar_docs = retrieve_from_db(texto)

    # Concatenar os documentos similares como contexto adicional
    context = "\n".join(similar_docs)

    # Preparar o prompt para o modelo (com contexto adicional)
    prompt = template_mensagem.format(
        texto=texto + "\n\nContexto relevante:\n" + context
    )

    # Gerar a resposta com o modelo
    response = chain.invoke({"texto": prompt})

    return response


# # Exemplo de interação com o chatbot
# if __name__ == "__main__":
#     user_input = input("Digite sua mensagem para o chatbot: ")

#     bot_response = process_user_input(user_input)
#     print(f"Resposta do Bot: {bot_response}")
