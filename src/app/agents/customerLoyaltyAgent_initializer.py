import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from tool_definitions import get_tools_for_agent_oneshot
from agent_initializer import initialize_agent
import asyncio

load_dotenv()
