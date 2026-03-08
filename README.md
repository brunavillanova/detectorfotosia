# 🤖 Detector de Imagens Geradas por IA

Um aplicativo web simples que permite enviar uma imagem e verificar se ela pode ter sido gerada por Inteligência Artificial.

O sistema utiliza **Python**, **Flask** e um modelo de visão computacional para analisar imagens enviadas pelo usuário.

---

## 🚀 Demonstração

O usuário pode:

* Enviar uma imagem
* O sistema analisa a imagem
* Exibe uma estimativa se a imagem foi gerada por IA ou se parece ser uma foto real

---

## 🛠️ Tecnologias utilizadas

* Python
* Flask
* PyTorch
* Torchvision
* Pillow
* HTML / CSS

---

## 📂 Estrutura do projeto

```
Detector/
├── .venv/
├── templates/
│   └── index.html
├── uploads/
├── app.py
└── README.md
```

---

## ⚙️ Instalação

Clone o repositório:

```
git clone git clone https://github.com/BrunaVillanova/detector-ia.git
```

Entre na pasta do projeto:

```
cd seuprojeto
```

Crie um ambiente virtual:

```
python -m venv .venv
```

Ative o ambiente:

Windows

```
.venv\Scripts\activate
```

Linux / Mac

```
source .venv/bin/activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

## ▶️ Executar o projeto

Para iniciar o servidor:

```
python app.py
```

Depois abra no navegador:

```
http://127.0.0.1:5000
```

---

## 📤 Como funciona

1. O usuário envia uma imagem
2. A imagem é salva temporariamente na pasta `uploads`
3. O modelo analisa a imagem
4. O sistema retorna uma probabilidade indicando se a imagem parece ser gerada por IA

---

## 📌 Observação

Este projeto é experimental e serve para fins educacionais. Detectar imagens geradas por IA com precisão é um desafio complexo e geralmente requer datasets grandes e modelos treinados especificamente para esse propósito.

---

## 👩‍💻 Autor

Projeto desenvolvido por Bruna.
