from fastapi import FastAPI 
import models
from database import engine
from routers import llm_calls
# from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# To limit where requests can from 
# origins = [
#     "local_host:5431",  # Replace with your streamlit app frontend url
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# add routers for the app here

app.include_router(llm_calls.router)