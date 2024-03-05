import os
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
from src.config import OAI_CONFIG_LIST
from src.gaiaprompts import 


dl = DataLoader()
#load dataset from Ragas
loader = DirectoryLoader("./src/your_files_here")
documents = loader.load()
# Ragas generator with openai models
generatoragas = TestsetGenerator.with_openai()
    for document in documents:
    document.metadata['filename'] = document.metadata['source']
# generate testset
testset = generatoragas.generate_with_langchain_docs(documents, test_size=10, distributions={simple: 0.5, reasoning: 0.25, multi_context: 0.25})
testset.to_pandas()
# # Use DSPY SytheticDataGenerator :
# # Generating synthetic data via a pydantic model
# generator = SyntheticDataGenerator(schema_class=SyntheticFacts)
# examples = generator.generate(sample_size=6)

# # Generating synthetic data via existing examples
generatordspy = SyntheticDataGenerator(examples=testset)
examples = generatordspy.generate(sample_size=5)
examples.to_pandas()
#refactor to take examples for each prompt !
