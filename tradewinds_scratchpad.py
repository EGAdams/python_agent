from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

key="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"
import os
os.environ["OPENAI_API_KEY"] = key


agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=2000 ),
    tool=PythonREPLTool(),
    verbose=True
)

prompt = """
Plese get the javascript MonitorLed object from this address:
https://americansjewelry.com/libraries/monitored-object/lib/MonitorLed.js

Please use this Python code to get the text:
``` python
import requests
url = 'https://americansjewelry.com/libraries/monitored-object/lib/MonitorLed.js'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}
r = requests.get(url, headers=headers)
print(r.text)
```
Translate the JavaScript text into a Python file.
Create another Python file to test this MonitorLed object.
Run the test
"""
agent_executor.run( prompt )