# Exchange V2

# 🌍 Real-Time Currency & Crypto Price Tracker

This project is a real-time price tracking platform for **global fiat currencies** and **cryptocurrencies**.  
It allows users to monitor up-to-date exchange rates and crypto prices through integrations with multiple external APIs.

## ✨ Features

- 📊 Real-time prices for **world currencies**
- ₿ Live tracking of **cryptocurrencies**
- 🔌 Integration with third-party APIs  
  - Binance API for cryptocurrency prices
- 🔐 Secure authentication using **OAuth 2.0**
- 🔑 Google API integration (Google OAuth)
- 📧 SMTP-based email verification  
  *(frontend implementation is still in progress)*

## 🛠 Tech Stack

### Backend
- **Python**
- **FastAPI**
- OAuth 2.0 authentication
- SMTP email service

### Frontend
- **JavaScript**
- **React.js**

## 🚧 Project Status

- Backend functionality is implemented
- Frontend is partially completed
- Email verification logic exists, UI is not finished yet

## 🎯 Goal

The main goal of this project is to provide a **fast, secure, and scalable** solution for tracking currency and cryptocurrency prices in real time using modern web technologies.

---

## 🚀 Launch

1. **Cloning repository**
   - Make sure you have [git](https://git-scm.com/downloads) installed
   - Open any shell on your machine
   - Clone repository
     ```
     git clone {repository url}  
     ```
   - Change current directory to created one
     ```
     cd {repository name}
     ```

2. **Environment variables setup**
   - Via code editor you need to create .env file in **backend** folder
   - You can use example-env.txt template to create it

3. **Installing and activating virtual environment**
   - Make sure that you have [uv](https://github.com/astral-sh/uv)
   - and any [python interpreter](https://www.python.org/downloads/) installed
   - Create virtual environment:
     ```
     uv venv
     ```
   - Activate your environment
     - Windows:
       ```
       .venv\Scripts\activate
       ```
     - Linux/macOS:
       ```
       source .venv/bin/activate
       ```
     - After this you can install all dependencies
       ```
       uv sync
       ```
   - To change python version you can use
    ```
    uv python pin {version} # 3.12 version by default
    ```
    To change version below **3.10** you will need to change field **required-python** in **pyproject.toml** file
    and after to do command upper

4. **Database setup**
   - To create all tables and db structure use
    ```
    alembic upgrade head
    ```
    or:
    ```
    uv run alembic upgrade head
    ```

5. **.pem keys setup**
   - For authorization and authentication on api you need to create public and private keys for jwt tokens
   - Make sure that you have openssl installed
    ```
    mkdir backend/src/keys
    ```
    ```
    openssl genpkey -algorithm RSA -out backend/src/keys/private_key.pem
    ```
    ```
    openssl rsa -in backend/src/keys/private_key.pem -pubout -out backend/src/keys/public_key.pem
    ```

6. **Backend setup**
   - Change current directory to "backend"
    ```
    cd backend
    ```
   - Install all mock data for database
    ```
    python -m scripts.db.data
    ```
    or:
    ```
    uv run python -m scripts.db.data
    ```

7. **Backend Launch**
   - To run app use
    ```
    python main.py
    ```
    or:
    ```
    uv run python main.py
    ```

8. **Backend logs checking**      
   - In **logs** folder you will find logs file for backend

---

# Great job! Enjoy!


