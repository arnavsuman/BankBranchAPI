from pydantic import BaseModel

class BranchSchema(BaseModel):
    ifsc: str
    bank_id: int
    branch: str
    address: str
    city: str
    district: str
    state: str

    class Config:
        orm_mode = True
