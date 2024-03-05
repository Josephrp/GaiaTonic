import os
import dspy
import ragas
import langchain
import chromadb
from dspy.datasets import DataLoader
from chromadb_rm import ChromadbRM
from langchain.document_loaders import DirectoryLoader
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from src.teams.teambuilder import TeamCompose
from src.teams.teamgraph import MultiTeamGraph
from src.agentics import AgentFactory
import src.config
import src.gaia-prompts


dl = DataLoader()
#load dataset from Ragas
loader = DirectoryLoader("./src/your_files_here")
documents = loader.load()
# Ragas generator with openai models
generator = TestsetGenerator.with_openai()
for document in documents:
    document.metadata['filename'] = document.metadata['source']
# generate testset
testset = generator.generate_with_langchain_docs(documents, test_size=10, distributions={simple: 0.5, reasoning: 0.25, multi_context: 0.25})
testset.to_pandas()

## global vars (move elsewhere)


## load models 


# # Define (DSPY) Predictor and Signature
# class GenerateAnswer(dspy.Signature):
#     """Answer questions given the context"""

#     context = dspy.InputField(desc="may contain relevant facts")
#     question = dspy.InputField()
#     answer = dspy.OutputField(desc="Answer the question in 1-5 words")

# class RAG(dspy.Module):
#     def __init__(self, num_passages=5):
#         super().__init__()
#         self.retrieve = dspy.Retrieve(k=num_passages)
#         self.generate_answer = dspy.ChainOfThought(GenerateAnswer)
    
#     def forward(self, question):
#         context = self.retrieve(question).passages
#         prediction = self.generate_answer(context=context, question=question)
#         return dspy.Prediction(context=context, answer=prediction.answer)
# run DSPy
# Main application logic