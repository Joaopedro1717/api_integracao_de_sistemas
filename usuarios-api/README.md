# 📘 usuarios-api

API para gerenciamento de usuários e equipes 

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) — Framework moderno e rápido para APIs em Python.
- [SQLModel](https://sqlmodel.tiangolo.com/) — ORM baseado em Pydantic e SQLAlchemy.
- [PostgreSQL](https://www.postgresql.org/) — Banco de dados relacional robusto.
- [Redis](https://redis.io/) — Armazenamento em memória utilizado para cache (opcional).
- [Uvicorn](https://www.uvicorn.org/) — Servidor ASGI de alta performance.

---

## 📁 Estrutura do Projeto

usuarios-api/
├── app/
│ ├── api/ # Rotas da API
│ ├── core/ # Configurações (DB, Redis)
│ ├── models/ # Modelos SQLModel
│ ├── repositories/ # Operações com o banco
│ ├── schemas/ # Schemas Pydantic para entrada/saída
│ └── services/ # Regras de negócio, cache etc.
├── main.py # Inicialização da aplicação FastAPI
├── requirements.txt # Dependências
└── README.md # Este arquivo


---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Joaopedro1717/api_integracao_de_sistemas.git
cd usuarios-api
```

### 2.Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### 3.Instale as dependências

pip install -r requirements.txt

### 4. Configure o banco de dados
Certifique-se de ter o PostgreSQL rodando e configure a string de conexão no arquivo
Utilize .env

### 5.(Opcional) Configure o Redis

No arquivo app/core/redis_client.py, defina a URL do Redis (ex: redis://localhost:6379/0).

### Executar a aplicação

```
uvicorn main:app --reload
```

A API estará disponível em:

http://127.0.0.1:8000

A documentação interativa do Swagger estará em:

http://127.0.0.1:8000/docs


🧪 Endpoints disponíveis
Equipes
POST /equipes/ — Criar equipe

GET /equipes/ — Listar equipes

Usuários
POST /usuarios/ — Criar usuário

GET /usuarios/ — Listar usuários

GET /usuarios/{nome} — Buscar usuário por nome