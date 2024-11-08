# Chatbot Interativo - Aprendizado Contínuo

Este projeto consiste em desenvolver um chatbot interativo que responda perguntas e aprenda com as interações do usuário, adaptando-se para fornecer uma experiência personalizada e contínua. O chatbot armazena informações relevantes sobre o tema com o qual interage, mas apenas quando forem consideradas verdadeiras e relevantes ou forem preferências do usuário.

---

## Funcionalidades e Objetivos

1. **Respostas Inteligentes e Aprendizagem Adaptativa**:
   - O chatbot responde às perguntas do usuário com base em uma linguagem de modelo (LLM) e adapta-se ao feedback do usuário, registrando informações apenas quando for verificado que são verdadeiras ou relevantes, como preferências específicas (por exemplo, usar tom formal).
   - Caso o usuário tente armazenar informações incorretas ou enganosas, o chatbot as rejeitará, reforçando a integridade dos dados armazenados.

2. **Interface Visual (UI)**:
   - Foi criada uma interface visual rápida e prática com o **Streamlit** para facilitar a interação com o chatbot. 
   - A UI é simples e responsiva, servindo para comunicação com o modelo e facilitando o ajuste das preferências do usuário.

3. **Uso de LangGraph e LangChain**:
   - **LangGraph** e **LangChain** são empregados para estruturar fluxos de conversa e integrar o aprendizado com o armazenamento em uma base de dados vetorial.
   - **LangChain** permite que o chatbot se conecte ao LLM e gerencie a memória e a lógica de decisão do bot.

4. **LLM (Large Language Model)**:
   - É possível usar qualquer LLM configurado via uma variável de ambiente para a chave da API. 

5. **Base de Dados Vetorial**:
   - Uma base de dados vetorial é usada para armazenar e gerenciar dados relevantes e preferências do usuário.
   - Essa base é executada em um container Docker, garantindo portabilidade e facilidade na configuração e implantação.

---

## Estrutura do Projeto

```bash
├── backend/
│   ├── app.py                    # UI do Streamlit
│   ├── chatbot.py                # Lógica principal do chatbot
│   ├── requirements.txt          # Dependências do backend
│   ├── Dockerfile                # Dockerfile para o backend
│   ├── server.py                 # Api do chatbot
│   └── start.sh                  # Script de inicialização do backend
├── chroma-db/
│   └── Dockerfile                # Dockerfile para o backend
├── docker-compose.yml            # Configuração dos serviços Docker (backend e base de dados vetorial)
└── README.md                     # Documentação do projeto
```

---
## Variáveis de Ambiente
Para configurar o LLM e a base de dados, utilize as seguintes variáveis de ambiente:

- CHROMA_HOST: O host da base de dados vetorial (definido no docker-compose como chroma-db).
- CHROMA_PORT: A porta da base de dados vetorial (definida como 8000).
- GROQ_API_KEY: A chave da API do LLM Groq utilizado, configurada através de variáveis de ambiente.

---
## Executando o Projeto
1. Passo 1: Clone o repositório e navegue até a pasta raiz do projeto.

``` sh
git clone https://github.com/jeffyuri7/chatbot.git
cd chatbot
```
2. Passo 2: Suba os containers Docker.

``` sh
docker-compose up --build
```
3. Passo 3: Acesse a interface visual no navegador:

``` sh
http://localhost:8501
```

---
## Como o Chatbot Armazena Dados
O chatbot utiliza LangChain e ChromaDB para armazenar dados de maneira seletiva e relevante, com as seguintes condições:

1. Informações Verdadeiras: Dados que são verificados como corretos.
2. Preferências do Usuário: Como tom de linguagem, formato de respostas, e outros ajustes de interação.

---
## Dependências
As dependências principais do backend estão listadas em requirements.txt e incluem:

- LangChain e LangGraph: Para estruturação e fluxo de diálogo.
- ChromaDB: Para armazenamento vetorial.
- Streamlit (para a interface visual).
