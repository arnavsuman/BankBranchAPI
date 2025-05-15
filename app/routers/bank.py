from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi.responses import HTMLResponse
from ..database import get_db
import sqlite3

router = APIRouter()


@router.get("/", response_class=HTMLResponse)         #Handles /  request also called Home Page request
def read_root():
    return """
    <html>
        <head>
            <title>BankBranchAPI</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
            <h1>Welcome to <span style="color:#2a9d8f;">BankBranchAPI</span> </h1>
            <p>Explore bank branches in India.</p>
            <p>based on the unwieldy (too big) excel file from <a href="http://rbidocs.rbi.org.in/rdocs/content/docs/68774.xls">RBI</a> </p>
            <p><strong>Endpoints:</strong></p>
            <ul style="list-style-type: none;">
                <li><a href="/branches">/branches</a> - List/search branches</li>
                <li><a href="/branches/ABHY0065001">/branches/{ifsc-code}</a> - Get branch by IFSC Code</li>
            </ul>
            <h2> © 2025 Arnav Suman. All rights reserved. Created as part of a take-home assignment.</h2>
        </body>
    </html>
    """


@router.get("/branches/{ifsc}", response_model=schemas.BranchSchema)         #Handles /brancehs/{ifsc} request
def get_branch(ifsc: str, db: Session = Depends(get_db)):
    branch = db.query(models.Branch).filter(models.Branch.ifsc == ifsc).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch


@router.get("/branches")    #Handles /brancehs request
def list_branches(
    bank_name: str = Query(None),
    city: str = Query(None),
    limit: int = 100,
    offset: int = 0
):
    params = []
    query = """
    SELECT branches.ifsc, branches.branch, branches.address, branches.city,
           branches.district, branches.state, banks.name as bank_name
    FROM branches
    JOIN banks ON branches.bank_id = banks.id
    """

    filters = []
    if bank_name:
        filters.append("banks.name LIKE ?")
        params.append(f"%{bank_name}%")

    if city:
        filters.append("branches.city LIKE ?")
        params.append(f"%{city}%")

    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    with sqlite3.connect("indian_banks.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        results = [dict(row) for row in rows]
        return results
