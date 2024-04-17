from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime
from typing import Optional, List
import uuid

# Create Article LLM


class CreateArticle(BaseModel):
    title: str
    topics: List[str]
    bulletPoints: List[List[str]]
    model: Optional[str] = 'gpt-3.5-turbo'


class CreateArticleOut(BaseModel):
    title: str
    body: str
    created_at: datetime
    updated_at: datetime
    id: uuid.UUID


# Generate Bullet Ponints
class GenerateBulletPoints(BaseModel):
    articleTitle: str
    topic: str
    number: int
    model: Optional[str] = 'gpt-3.5-turbo'
