import langchain
import chromadb
import dspy
from dspy.datasets import DataLoader
from dspy.experimental import SyntheticDataGenerator
from chromadb_rm import ChromadbRM

from langchain.document_loaders import DirectoryLoader
import ragas
from ragas.ragas.testset.generator import TestsetGenerator
from ragas.ragas.testset.evolutions import simple, reasoning, multi_context
import autogen 
from autogen import config_list_from_json
from src.teams.teambuilder import TeamCompose
from src.teams.teamgraph.gaiagraph import GroupChatFSM , MultiTeamGraph
from src.agentics.agentlist import AgentFactory
from src.config
from src.gaiaprompts
from src.promptcompiler.compiler import 
import os
import json
from dotenv import load_dotenv

## global vars (move elsewhere)
load_dotenv()

# Initialize configurations and group chat FSM with three teams based on the configuration
configurations = config_list_from_json(config_json_content)
group_chat_fsm = GroupChatFSM(configurations)
## load models 


# Main application logic



