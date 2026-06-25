import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from langchain.messages import HumanMessage
from langchain.tools import tool
from datetime import datetime

load_dotenv()


@tool
def current_time():
    """Returns the current date and time."""
    return str(datetime.now())

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

tool = TavilySearch(
    max_results=5,
    topic="general",
)

agent = create_agent(
    model=model,
    tools=[tool,current_time]
)

messages = []

while True:
    user_input = input("Enter here: ")

    if user_input.lower() == "quit":
        break

    messages.append(HumanMessage(content=user_input))

    response = agent.invoke({"messages": messages})

    ai_message = response["messages"][-1]

    output = response["messages"][-1]

    if isinstance(output.content, list):
        print(output.content[0]["text"])
    else:
        print(output.content)

    messages.append(ai_message)