# 🏦 BankBranchAPI - Indian Bank Branch API

BankPAI is a FastAPI-powered REST API for retrieving branch details of Indian banks using IFSC codes and search queries. It is backed by a SQLite database (`indian_banks.db`) and provides endpoints for getting branch information, searching by city, and more.

### 🌐 Hosted Live On Render
🔗 [https://bankbranchapi.onrender.com](https://bankbranchapi.onrender.com)

---

## 🚀 Features

- Get branch details using IFSC code
- Search branches by city or with pagination
- Filter results by city with limit and offset
- Clean and minimal JSON responses
- Fully tested using Pytest

---

## 🗂️ Endpoints

------------------------------------------------------------------------------------
| Method | Endpoint                          | Description                         |
|--------|-----------------------------------|-------------------------------------|
| GET    | `/`                               | Welcome homepage                    |
| GET    | `/branches/{ifsc_code}`           | Get branch details by IFSC          |
| GET    | `/branches?city=MUMBAI`           | Search branches by city             |
| GET    | `/branches?limit=10&offset=0`     | Paginated branches list             |
| GET    | `/branches?city=MUMBAI&limit=10`  | Combined filters                    |
------------------------------------------------------------------------------------
---

## 🛠️ Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/bankbranchapi.git
cd bankbranchapi
```
### 1.  Install Requirements
