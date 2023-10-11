#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model representing the 'users' table.

    Attributes:
    - id: INTEGER (auto-incremented primary key)
    - email: VARCHAR(250)
    - hashed_password: VARCHAR(250)
    - session_id: VARCHAR(250) (nullable)
    - reset_token: VARCHAR(250) (nullable)
    """
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    email = Column(String(length=250), nullable=False)
    hashed_password = Column(String(length=250), nullable=False)
    session_id = Column(String(length=250), nullable=True)
    reset_token = Column(String(length=250), nullable=True)
