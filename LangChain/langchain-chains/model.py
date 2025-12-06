from langchain_google_genai import ChatGoogleGenerativeAI
import os
import sys
sys.path.insert(0, "g:/GenAI")
from config import GEMINI_API_KEY, GEMINI_MODEL

# Set the API key
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)

result = model.invoke('What is the capital of India')

print(result.content)