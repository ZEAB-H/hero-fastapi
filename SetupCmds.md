# 🚀 FastAPI Project Setup

This guide walks you through setting up and running the FastAPI project from scratch.

---

## 🖥️ Prerequisites
- Python 3.10+
- Git

---

## ⚡ Setup Instructions (Windows, macOS, Linux)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-fastapi-project.git
cd 

---

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv .venv
```

#### On Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

#### On macOS / Linux:

```bash
source .venv/bin/activate
```

---

### 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

*(If `requirements.txt` is missing, install manually with:)*

```bash
pip install fastapi uvicorn
```

---

### 5. Ignore Virtual Environment from Git

```bash
"*" > .venv/.gitignore
```

---

### 6. Verify Python Installation

```bash
python --version
pip --version
```

---

### 7. Run the FastAPI Development Server

```bash
fastapi dev main.py
```

Server runs at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### 8. Deactivate Virtual Environment

```bash
deactivate
```

---

## 📖 Useful Endpoints

* Swagger Docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📦 Project Structure (Suggested)

```
.
├── .venv/              # Virtual environment
├── app/                # FastAPI application code
│   ├── main.py         # Entry point
│   ├── routers/        # API routes
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic schemas
│   └── services/       # Business logic
├── requirements.txt    # Dependencies
└── README.md           # Setup instructions
```

 

 ### Database Related 


```commandline
psql -U postgres
```
default password for the starter
```bash
password= postgres
```


## Database Command Lines 

```bash 
\l  --> For listing the databases
CREATE DATABASE hero_db;    --> For Creating A DATABASE
CREATE USER abel WITH PASSWORD 'Test1234'; -> For Creating a User with role
GRANT ALL PRIVILEGES ON DATABASE hero_db TO abel; -> To Grant all Privillages
\c hero_db; --> To connect to the Database
GRANT USAGE ON SCHEMA public TO abel; 
GRANT CREATE ON SCHEMA public TO abel;

\q -> to quit and return to terminal
 



```


## General App Commands

```commandline
 fastapi dev main.py  # to start the server 

```