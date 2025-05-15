# 🏦 BankBranchAPI - Indian Bank Branch API

BankPAI is a FastAPI-powered REST API for retrieving branch details of Indian banks using IFSC codes and search queries. It is backed by a SQLite database (`indian_banks.db`) and provides endpoints for getting branch information, searching by city, and more.

### 🌐 Hosted Live On Render
🔗 [https://bankbranchapi.onrender.com](https://bankbranchapi.onrender.com)


## Features

- Get branch details using IFSC code
- Search branches by city or with pagination
- Filter results by city with limit and offset
- Clean and minimal JSON responses
- Fully tested using Pytest

## Endpoints

| Method | Endpoint                          | Description                         |
|--------|-----------------------------------|-------------------------------------|
| GET    | `/`                               | Welcome homepage                    |
| GET    | `/branches/`                      | Get branch List                     |
| GET    | `/branches/{ifsc_code}`           | Get branch details by IFSC          |
| GET    | `/branches?city=MUMBAI`           | Search branches by city             |
| GET    | `/branches?limit=10&offset=0`     | Paginated branches list             |
| GET    | `/branches?city=MUMBAI&limit=10`  | Combined filters                    |


##  Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/bankbranchapi.git
cd bankbranchapi
```
### 2.  Install Requirements
```bash
pip install -r requirements.txt
```
### 3. Ensure .db File Is Present

Place indian_banks.db inside the root or app directory (where the code looks for it).

### 3. All Set. Run the API Locally
```bash
uvicorn app.main:app --reload
```
---

### Then visit 

Swagger UI:
```bash
http://127.0.0.1:8000/docs
```
Root Page: 
```bash
http://127.0.0.1:8000/ 
```

---

## RUNNING TESTS
Tests are located in the bankbranchapi/tests/test_api.py

### To run tests:

### 1. Go to root folder 

```bash
cd bankbranchapi
```
### 2. Execute

```bash
python -m pytest tests/test_api.py
```

---
## Deployment on Render

The API is hosted on Render using Gunicorn + Uvicorn workers.

Home Page - [https://bankbranchapi.onrender.com](https://bankbranchapi.onrender.com)
Branch List - [https://bankbranchapi.onrender.com/branches](https://bankbranchapi.onrender.com/branches)
Branch  by IFSC Code - [https://bankbranchapi.onrender.com/branches/ABHY0065001](https://bankbranchapi.onrender.com/branches/ABHY0065001)
Branches by city - [https://bankbranchapi.onrender.com/branches?city=MUMBAI](https://bankbranchapi.onrender.com/branches?city=MUMBAI)
Paginated Branches list - [https://bankbranchapi.onrender.com/branches?limit=10&offset=0](https://bankbranchapi.onrender.com/branches?limit=10&offset=0)
Combined filters - [https://bankbranchapi.onrender.com/branches?city=MUMBAI&limit=10](https://bankbranchapi.onrender.com/branches?city=MUMBAI&limit=10)

---
# Made by Arnav Suman.
For queries or contributions, feel free to open an issue or a pull request.
