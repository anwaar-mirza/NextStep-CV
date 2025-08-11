from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from essesntials import cv_prompt
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

class CVMakerBackend:
    def __init__(self):
        llm = self.crate_llm()
        prompt = self.create_prompt()
        parser = StrOutputParser()
        self.chain = prompt | llm | parser

    def crate_llm(self):
        return ChatGroq(model='llama-3.3-70b-versatile')
    
    def create_prompt(self):
        return ChatPromptTemplate.from_template(cv_prompt)