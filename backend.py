from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from essesntials import cv_prompt
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

class CVMakerBackend:
    def __init__(self):
        llm = self.crate_llm()
        prompt = self.create_prompt()
        parser = StrOutputParser()
        self.chain = prompt | llm | parser

    def crate_llm(self):
        return ChatOpenAI(model='gpt-4o-mini')
    
    def create_prompt(self):
        return ChatPromptTemplate.from_template(cv_prompt)