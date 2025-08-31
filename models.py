from __future__ import annotations
from typing import Optional, Union  # Add this import
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: Optional[int] = Field(default=None, index=True)
    secret_name: str