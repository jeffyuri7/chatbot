# Usar imagem base do Python
FROM python:3.12.7-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos necessários
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Copiar o script de inicialização
COPY start.sh /app/start.sh

# Tornar o script executável
RUN chmod +x /app/start.sh

# Expor as portas para as duas aplicações
EXPOSE 8501

# Comando para rodar o script
CMD ["/app/start.sh"]
