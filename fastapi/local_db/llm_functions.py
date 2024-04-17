from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import random


def call_llm(article: str, topic: str, bullet_points: str, openai_api_key: str, model: str = 'gpt-3.5-turbo'):
    print("Creating OpenAI....")
    template = """
    Write the next paragraph in the following article: {article}. DO NOT DEVIATE AWAY FROM THE BULLET POINTS. MAKE SURE TO ONLY INCLUDE FACTUAL INFORMATION IN THE BULLET POINTS. HOWEVER YOU ARE ALLOWED TO ELABORATE.

    Paragraph Topic: {topic}
    Bullet Points: {bullet_points}
    """
    prompt = ChatPromptTemplate.from_template(template)

    model = ChatOpenAI(api_key=openai_api_key, temperature=0, model=model)

    chain = (
        {"article": RunnablePassthrough(), "topic": RunnablePassthrough(),
         "bullet_points": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    response = chain.invoke(
        {"article": article, "topic": topic, "bullet_points": bullet_points})

    return response


def generate_bullet_points_llm(article_title: str, paragraph_topic: str, number: int, openai_api_key: str, model: str = 'gpt-3.5-turbo'):

    generate_bullet_points_prompt = """

    You are an assistant for an article writer and editor. The Article Title is {article_title}. Your job is to come up with potential bullet points to help format a paragraph with the following topic {paragraph_topic}. The bullet points should be elaborated to make coherent points for the whole paragraph. CREATE {number} of Bullet Points no more no less. ONLY PROVIDE THE BULLET POINTS AS SENTENCES FOR THE A RESPONSE. DO NOT NUMBER THEM OR DEMARCATE THEM IN ANY WAY. DO NOT PROVIDE ANY OTHER RESPONSE:


    """

    prompt = ChatPromptTemplate.from_template(generate_bullet_points_prompt)

    model = ChatOpenAI(api_key=openai_api_key, temperature=random.random(
    ) ** .7, model=model)  # Random Temperature with a .7 skew

    chain = (
        {"article_title": RunnablePassthrough(
        ), "paragraph_topic": RunnablePassthrough(), "number": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    response = chain.invoke({"article_title": article_title,
                            "paragraph_topic": paragraph_topic, "number": number})

    return response
