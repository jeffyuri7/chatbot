# Usar uma imagem base do Python
FROM python:3.12.7-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev

# Definir diretório de trabalho
WORKDIR /app

# Instalar Chroma e suas dependências
RUN pip install chromadb

# Copiar o código da aplicação
COPY . .

# Expor a porta para o serviço
EXPOSE 5000

# Comando para iniciar o Chroma com a porta e o caminho especificados
CMD ["chroma", "run", "--port", "5000", "--path", "/app/db"]
