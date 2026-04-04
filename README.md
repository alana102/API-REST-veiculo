# API REST - Gerenciamento de Frota de Veículos

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-00A8E1?style=for-the-badge&logo=databricks)
![uv](https://img.shields.io/badge/uv-Fast-purple?style=for-the-badge)

Trabalho acadêmico desenvolvido para criar uma API RESTful de veículos.

---

## Tecnologias Utilizadas

A arquitetura do trabalho foi desenhada separando as responsabilidades (Rotas, Modelos e Banco de Dados), utilizando as seguintes ferramentas:

* **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno e ultrarrápido para a construção das rotas da API, com geração automática de documentação (Swagger UI).
* **[Delta Lake](https://delta.io/) & [PyArrow](https://arrow.apache.org/):** Sistema de armazenamento colunar para persistência dos dados em arquivos `.parquet`, permitindo leituras eficientes e processamento em lotes (*batches*).
* **[Pandas](https://pandas.pydata.org/):** Biblioteca essencial para a manipulação e filtragem dos dados extraídos do Delta Lake.
* **[Pydantic](https://docs.pydantic.dev/):** Utilizado para a modelagem estrita e validação dos dados de entrada (JSON) recebidos nas requisições.
* **[uv](https://github.com/astral-sh/uv):** Gerenciador de pacotes e ambientes virtuais em Python, escrito em Rust, que garante uma instalação e execução extremamente rápidas.

---

## Principais Funcionalidades

* **CRUD Completo:** Criação, leitura, atualização e remoção de veículos.
* **Paginação e Contagem:** Consultas otimizadas no Delta Lake para listar veículos em páginas e retornar o volume exato.
* **Exportação em Streaming:** Geração de relatórios completos do banco de dados em **CSV** e compactados em **ZIP** (`/exportar/csv` e `/exportar/zip`). Os dados são processados em pedaços (*chunks*) diretamente do disco para o cliente.

---

## Como Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.12+** instalado na sua máquina, além do gerenciador de pacotes **uv**.
Para instalar o `uv`, siga a [documentação oficial](https://github.com/astral-sh/uv).

### Passo a Passo

**1. Clone o repositório e entre na pasta do projeto:**
```bash
git clone https://github.com/seu-usuario/API-REST-veiculo.git
cd API-REST-veiculo
```

**2. Sincronize as dependências do projeto:**
*(O `uv` vai ler o arquivo uv.lock e baixar tudo automaticamente)*
```bash
uv sync
```

**3. Inicie o Servidor da API:**
```bash
uv run fastapi dev src/api/main.py
```

**4. Povoe o Banco de Dados (Gerar dados de teste):**
Execute o script abaixo para criar a pasta do Delta Lake e injetar veículos fictícios (Hondas, Yamahas, etc.) para teste:
```bash
uv run python src/database/povoando.py
```

**5. Acesse a Documentação Interativa:**
Com o servidor rodando, abra o seu navegador e acesse o Swagger UI para testar todas as rotas com um clique:
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 📁 Estrutura de Pastas

```text
API-REST-veiculo/
├── src/
│   ├── api/                # Endpoints e inicialização do FastAPI (main.py, rotas)
│   ├── database/           # Conexão Delta Lake e scripts de povoamento (seed)
│   └── models/             # Modelos de validação Pydantic (veiculo_model.py)
├── pyproject.toml          # Configurações do projeto e dependências
├── uv.lock                 # Trava de versões do gerenciador uv
└── README.md               # Documentação do projeto
```