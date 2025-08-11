from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    """Base model class with common fields for all models"""
    __abstract__ = True
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False) 