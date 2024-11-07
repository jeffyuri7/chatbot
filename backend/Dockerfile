# Usar imagem base do Python
FROM python:3.12.7-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev

# Definir diretório de trabalho
WORKDIR /app

# Copiar o arquivo de requisitos para instalação das dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . .

# Copiar o script de inicialização
COPY start.sh /app/start.sh

# Tornar o script executável
RUN chmod +x /app/start.sh

# Expor a porta necessária para a comunicação
EXPOSE 8501

# Definir o comando para rodar o container
CMD ["/app/start.sh"]
