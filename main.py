
import dspy
import ragas
import langchain
import chromadb
from dspy.datasets import DataLoader
from dspy.dspy.experimental import SyntheticDataGenerator
from chromadb_rm import ChromadbRM
from langchain.document_loaders import DirectoryLoader
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from src.teams.teambuilder import TeamCompose
from src.teams.teamgraph import MultiTeamGraph
from src.agentics import AgentFactory
import src.config
import src.gaiaprompts
import src.promptcompiler 
import os
import json



## global vars (move elsewhere)

# Initialize configurations, agents, and group chat environment based on the sample configuration

# Initialize configurations and group chat FSM with three teams based on the configuration
configurations = config_list_from_json(config_json_content)
group_chat_fsm = GroupChatFSM(configurations)
## load models 


# Main application logic



