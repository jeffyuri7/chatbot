#!/usr/bin/env python3
import chromadb

# from langchain_openai import OpenAIEmbeddings

# Criar ou carregar o banco de dados vetorial
client = chromadb.Client()

# A coleção pode ser a "base de dados" onde seus vetores são armazenados
collection = client.create_collection("user_data")


# Inserção de um exemplo de embedding (embora você adicione ao banco de dados quando fizer o `store_vector_in_db`)
def add_data_to_chroma(text):
    embedding = OpenAIEmbeddings()  # Usando OpenAI para gerar embeddings
    vector = embedding.embed_query(text)

    collection.add(
        documents=[text], metadatas=[{"source": "example"}], embeddings=[vector]
    )


# Servir o Chroma (sem necessidade de servidor adicional)
# add_data_to_chroma("Exemplo de texto armazenado no Chroma")
