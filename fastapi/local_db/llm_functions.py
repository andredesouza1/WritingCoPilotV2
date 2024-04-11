from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def call_llm(article:str, topic:str, bullet_points:str, openai_api_key:str, model:str = 'gpt-3.5-turbo'):
    print("Creating OpenAI....")
    template = """
    Write the next paragraph in the following article: {article}. DO NOT DEVIATE AWAY FROM THE BULLET POINTS. MAKE SURE TO ONLY INCLUDE FACTUAL INFORMATION IN THE BULLET POINTS. HOWEVER YOU ARE ALLOWED TO ELABORATE.

    Paragraph Topic: {topic}
    Bullet Points: {bullet_points}
    """
    prompt = ChatPromptTemplate.from_template(template)

    model = ChatOpenAI(api_key = openai_api_key, temperature = 0, model = model)

    chain = (
        {"article": RunnablePassthrough(), "topic": RunnablePassthrough(), "bullet_points": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    response = chain.invoke({"article": article, "topic": topic, "bullet_points": bullet_points})

    return response


def call_local_llm(article:str, topic:str, bullet_points:str, openai_api_key:str):
    """
    For Dev Purposes
    """
    
    print("CallingLocalLLM....")
    template = """
    Write the next paragraph in the following article: {article}. DO NOT DEVIATE AWAY FROM THE BULLET POINTS. MAKE SURE TO ONLY INCLUDE FACTUAL INFORMATION IN THE BULLET POINTS. HOWEVER YOU ARE ALLOWED TO ELABORATE.

    Paragraph Topic: {topic}
    Bullet Points: {bullet_points}
    """
    prompt = ChatPromptTemplate.from_template(template)

    model = ChatOpenAI(base_url="http://localhost:1235/v1", api_key = openai_api_key, temperature = 0)

    chain = (
        {"article": RunnablePassthrough(), "topic": RunnablePassthrough(), "bullet_points": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    response = chain.invoke({"article": article, "topic": topic, "bullet_points": bullet_points})

    return response    