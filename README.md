📝 Assignment Breakdown
You were asked to build an API service that interacts with a Bank Branches Database, and you had two choices:

GraphQL API – Expose a /gql endpoint with queries to get branches and their banks.

REST API – Create REST endpoints to:

Get a list of all banks

Get branch details for a specific IFSC code

You chose the REST API option.

Additionally:

🧼 Clean code = Bonus

✅ Test cases = Bonus

🚀 Deployment (like Heroku) = Bonus

✅ What the Code Does (in Simple Terms)
We’ve built a RESTful API using FastAPI and structured it in a modular way. Here's a full walkthrough:

🔧 1. Database Design (SQLAlchemy ORM)
We define two tables:

a. Bank Table
Stores bank names.

id is the primary key.

b. Branch Table
Stores branches of banks with:

ifsc code (unique branch ID)

Address, city, district, state

bank_id foreign key → links to Bank.id

plaintext
Copy
Edit
Bank
 └──<1---∞>── Branch

🚀 2. API Features
/banks/
Returns a list of all banks.

Example response:

```json

[
  {
    "id": 1,
    "name": "State Bank of India"
  },
  {
    "id": 2,
    "name": "HDFC Bank"
  }
]
```
/branches/{ifsc}
Returns details of a specific branch, including its bank's name.

Example request:

```bash

GET /branches/ABCD1234567
```
Example response:

```json
{
  "ifsc": "ABCD1234567",
  "branch": "Koramangala",
  "address": "12th Main, Bangalore",
  "city": "Bangalore",
  "district": "Bangalore Urban",
  "state": "Karnataka",
  "bank_id": 1,
  "bank": {
    "id": 1,
    "name": "State Bank of India"
  }
}
```


🛠 3. Folder & Code Explanation
app/models.py
Defines SQLAlchemy ORM models (Bank, Branch) for database interaction.

app/database.py
Sets up the SQLite database and SQLAlchemy session.

app/schemas.py
Defines Pydantic models for validating request/response JSONs.

app/routers/bank.py
Contains the API logic:

Connect to DB

Fetch bank/branch info

Return as JSON

app/main.py
Initializes FastAPI app

Sets up DB

Mounts router

tests/test_api.py
Unit tests using FastAPI’s built-in test client.

🧪 4. Testing
Test cases do two things:

Call /banks/ and check we get a valid list

Call /branches/{ifsc} and verify:

Either the correct branch is returned

Or 404 is returned if IFSC doesn’t exist

🚀 5. Heroku Deployment
Using the Procfile, the app can be deployed to Heroku easily:

```bash

web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-8000}
```
When pushed to Heroku:

It starts the API server using uvicorn

You get a public URL to access the endpoints

🧠 Summary
Component	Purpose
FastAPI	Build and serve API
SQLAlchemy	ORM for DB operations
SQLite	Lightweight DB
Pydantic	Validate API data
TestClient	Test API endpoints
/banks/	Get list of all banks
/branches/{ifsc}	Get details for one branch
Heroku setup	For cloud deployment


TO RUNN THE PREGIVEN TESTS 
```bash
python -m pytest -v tests/test_api.py 
```