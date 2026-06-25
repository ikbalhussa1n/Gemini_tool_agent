# Gemini Tool Agent 🤖

A lightweight AI agent built with LangChain and Google Gemini (2.5
Flash) that can use external tools like web search (Tavily) and system
utilities (e.g., current time/date) to answer user queries
intelligently.

## Features

-   Powered by Google Gemini 2.5 Flash
-   Web search using Tavily API
-   Custom tools (time/date)
-   Terminal-based chat loop
-   Agent-based tool usage

## Setup

### Install dependencies

pip install -r requirements.txt

### Environment variables

GOOGLE_API_KEY=your_key TAVILY_API_KEY=your_key

## Run

python main.py
