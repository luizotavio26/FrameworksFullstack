<h1 align="center">API Gerenciador de Tarefas</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

---

## 🚀 Sobre o Projeto
Este projeto é uma **API de gerenciamento de tarefas** desenvolvida em **Python** usando o framework **Flask**. A aplicação pode ser executada tanto localmente quanto dentro de um container Docker, facilitando o desenvolvimento e a implantação.

---

## 👩‍💻 Entrega
Atividade para a entrega no dia 12/09/2025 - como continuação das partes anteriores
**Código na pasta: Conteinerização-do-gerenciador-de-tarefas**

---

## ⚙️ Pré-requisitos
Para rodar a aplicação, certifique-se de que você tem as seguintes dependências instaladas em sua máquina:
* **Python 3.11+**
* **Docker**

---

## ▶️ Rodando a API

### Localmente
1.  Clone o repositório:
    ```bash
    git clone https://github.com/luizotavio26/FrameworksFullstack
    cd FrameworksFullstack
    cd Conteinerização-do-gerenciador-de-tarefas
   
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute o servidor:
    ```bash
    python app.py
    ```
    A API estará disponível em: [http://127.0.0.1:5002]

### Com Docker
1.  Construa a imagem:
    ```bash
    docker build -t tasks-api .
    ```
2.  Execute o container:
    ```bash
    docker run -d -p 5002:5002 tasks-api
    ```

---

## 👩‍💻 Autores

Ana Beatriz Silva Santos

Luiz Otávio Santos Silva

Murillo Rodrigues Santos Pereira

Uatila dos Santos Silva
