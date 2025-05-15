from sqlalchemy import Column, String, Integer
from .database import Base

class Branch(Base):
    __tablename__ = "branches"

    ifsc = Column(String, primary_key=True, index=True)
    bank_id = Column(Integer)
    branch = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)
