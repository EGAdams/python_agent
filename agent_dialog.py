from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

key="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"
import os
os.environ["OPENAI_API_KEY"] = key


agent_executor = create_python_agent(
    llm=OpenAI(temperature=0.2, max_tokens=3000 ),
    tool=PythonREPLTool(),
    verbose=True
)

prompt = """
Please create a Python-based command line chatbot application that takes user input from stdin 
and provides responses based on the user's input. The chatbot should store conversation history in
a vecotor store like faiss for future conversations. 

To accomplish this, please follow these steps:

Create a directory structure for the application on this chromebook.
Write all of the code that we need and put it inside the directory structure where they belong.
Please ensure that the application is built using SOLID principles.
Use GoF design patterns where appropriate.
"""
agent_executor.run( prompt )