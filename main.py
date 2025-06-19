"""
Account Service - Main application entry point
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import uuid

app = FastAPI(title="Account Service", version="1.0.0")


class AccountCreate(BaseModel):
    customer_name: str
    email: EmailStr
    account_type: str
    initial_deposit: float


class AccountResponse(BaseModel):
    account_id: str
    customer_name: str
    account_type: str
    balance: float
    status: str
    created_at: datetime


@app.post("/accounts", response_model=AccountResponse)
async def create_account(account: AccountCreate):
    """Create a new bank account"""
    if account.initial_deposit < 0:
        raise HTTPException(status_code=400, detail="Initial deposit cannot be negative")
    
    account_id = str(uuid.uuid4())
    return AccountResponse(
        account_id=account_id,
        customer_name=account.customer_name,
        account_type=account.account_type,
        balance=account.initial_deposit,
        status="active",
        created_at=datetime.now()
    )


@app.get("/accounts/{account_id}")
async def get_account(account_id: str):
    """Get account details"""
    return {
        "account_id": account_id,
        "customer_name": "John Doe",
        "balance": 5000.00,
        "status": "active"
    }


@app.get("/accounts/{account_id}/balance")
async def get_balance(account_id: str):
    """Get account balance"""
    return {
        "account_id": account_id,
        "balance": 5000.00,
        "currency": "USD"
    }


# Release 1, Commit 1

# Release 1, Commit 2

# Release 1, Commit 3

# Release 1, Commit 4

# Release 1, Commit 5

# Release 1, Commit 6

# Release 1, Commit 7

# Release 1, Commit 8

# Release 1, Commit 9

# Release 1, Commit 10

# Release 1, Commit 11

# Release 2, Commit 1

# Release 2, Commit 2

# Release 2, Commit 3

# Release 2, Commit 4

# Release 1, Commit 1

# Release 1, Commit 2

# Release 1, Commit 3

# Release 1, Commit 4

# Release 1, Commit 5

# Release 1, Commit 6

# Release 1, Commit 7

# Release 1, Commit 8

# Release 1, Commit 9



# Add account data models (BANKACC-1)
# Implementation step 1 of 5
