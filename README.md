# Language Translator

A web-based language translation application powered by Hugging Face's MarianMT models. This project consists of a Flask-based backend and a Streamlit-based frontend, allowing users to easily translate text between various languages.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

##  Introduction

This project utilizes pre-trained MarianMT models from Hugging Face to perform machine translation between different language pairs. The backend handles API requests and translation logic, while the frontend provides a user-friendly interface for text input and result display.

---

##  Features

- Translate text between a wide range of languages
- Simple REST API (`/translate`)
- Clean and interactive Streamlit frontend
- Real-time translation results
- Uses powerful Hugging Face `transformers` and `torch`

---

##  Installation

Ensure you have Python 3.11 or higher installed.

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd translator
```

### 2. Set up backend

```bash
cd backend
poetry install
poetry run python main.py
```

### 3. Set up Frontend
Open a new terminal:

```bash
cd frontend
poetry install
poetry run streamlit run app.py
```

## Usage

1. Run the backend Flask server.

2. Launch the Streamlit app.

3. Enter text, source language code (e.g., en for English), and target language code (e.g., fr for French).

4. Click Translate and view the result.

## Configuration

- Backend API endpoint is set to http://127.0.0.1:5000/translate by default.

- You can modify BACKEND_URL in app.py if deploying to a different server.


## Dependencies

**Backend (pyproject.toml)**

- transformers

- torch

- sentencepiece

- flask

- flask-cors

- requests

- python-dotenv

---

**Frontend (pyproject.toml)**

- streamlit

- requests

- python-dotenv

All dependencies are managed via Poetry.

---

## Troubleshooting

- **Model not loading?**

    - Ensure internet access for downloading models from Hugging Face.

- **Translation fails?**

    - Check if the correct language codes are provided.

- **CORS issues?**

    - flask-cors is enabled in main.py, but validate browser/network configurations.


## Screenshots

![App Screenshot][def]

![App Screenshot][def2]

[def]: ./assets/trans1.png

[def2]: ./assets/trans2.png



