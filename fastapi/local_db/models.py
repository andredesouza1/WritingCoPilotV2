
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean, Interval
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import text
from sqlalchemy import create_engine, Column, Integer, String, Sequence, DateTime, Boolean, ForeignKey,Text, Table
import uuid

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    