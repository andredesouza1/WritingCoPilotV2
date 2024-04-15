from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
import schemas
from typing import List
from utils import create_queue, process_queue
import random
import os
from dotenv import load_dotenv

# This is for local testing only(Need to figure out a secure way to do this later)
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter(
    prefix="/llm_calls",
    tags=['LLM_Calls']
)



# @router.post("/create_article", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateArticleOut)
@router.post("/create_article", status_code=status.HTTP_201_CREATED)
def create_article(input: schemas.CreateArticle):
    """
    Create Article uses an LLM to create the an Article iterativly using bullet points as a guide similar to an outline.
    Creates a queue and then processes that queue in order building the article as it dequeues paragraphs info from the queue.
    
    """
    # Create the queue using the topics and bullet points as proxy for # of paragraphs
    my_queue = create_queue(input.topics,input.bulletPoints)

    article, paragraphs, bullet_point_list = process_queue(my_queue, openai_api_key, input.model)

    return article,paragraphs,bullet_point_list


@router.post("/create_article/test", status_code=status.HTTP_201_CREATED)
def create_article_test(input: schemas.CreateArticle):
    print(input.topics)
    print(input.bullet_points)