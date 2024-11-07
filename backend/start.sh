#!/bin/bash

# Rodar o servidor Python em segundo plano
python server.py --server.port=8000 &

# Rodar o Streamlit (vai rodar na porta 8501)
streamlit run app.py --server.port=8501
