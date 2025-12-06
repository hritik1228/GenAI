import os
import sys
sys.path.insert(0, "g:/GenAI")
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import GEMINI_API_KEY, GEMINI_MODEL

# Set the API key
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()