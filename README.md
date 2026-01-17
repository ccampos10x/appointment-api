# Appointment API

API REST desenvolvida em **Python** utilizando **FastAPI**, com foco em organização, escalabilidade e boas práticas para backend.

Esta API foi estruturada para servir como base profissional de projetos backend, com separação clara de responsabilidades, uso de virtual environment e versionamento via Git.

---

## 🚀 Tecnologias Utilizadas

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy (se aplicável)
* Virtualenv (`venv`)
* Git

---

## 📂 Estrutura do Projeto

```text
appointment-api/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── users.py
│   │   └── __init__.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── core/
├── venv/               # NÃO versionado
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd appointment-api
```

### 2. Criar e ativar o virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / MacOS
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando a API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

---

## 📑 Documentação Automática

FastAPI gera documentação automaticamente:

* Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```

* ReDoc:

  ```
  http://127.0.0.1:8000/redoc
  ```

---

## 📌 Rotas (Exemplo)

### Usuários

* `GET /users` — Lista usuários
* `POST /users` — Cria usuário
* `GET /users/{id}` — Detalha usuário
* `PUT /users/{id}` — Atualiza usuário
* `DELETE /users/{id}` — Remove usuário

*(Ajuste conforme as rotas reais do projeto)*

---

## 🧪 Testes (Opcional)

Caso utilize testes:

```bash
pytest
```

---

## 📦 Versionamento

* O diretório `venv/` **não é versionado**.
* Apenas código-fonte e arquivos de configuração sobem para o Git.

---

## 🧠 Boas Práticas Adotadas

* Separação por camadas (router, service, model, schema)
* Tipagem forte com Pydantic
* Virtual environment isolado
* Estrutura pronta para escalar

---

## 📄 Licença

Projeto para fins educacionais e profissionais.

---

## ✍️ Autor

Caio Campos
