from langchain_google_genai import ChatGoogleGenerativeAI
import sys
import os
sys.path.insert(0, "g:/GenAI")
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import GEMINI_API_KEY, GEMINI_MODEL

# Set the API key
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Unemployment in India'})

print(result)

chain.get_graph().print_ascii()