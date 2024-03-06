# Set up Ollama locally before testing/running this script
# On Ollama input "ollama run dolphin-phi" then /save dolphin-phi

import os
from transformers import pipeline

# Update paths and model names as needed
oll_model_name = "dolphin-phi"
oll_path = r"C:\Users\caleb\.ollama\models\manifests\registry.ollama.ai\library\dolphin-phi\latest" 
# path to your ollama ^
output_folder = r"C:\Users\caleb\.ollama\LEAPagAgentoutput"
master_prompt = "You are an agricultural assistant commited to regenerative practices. You are being supplied with a list of tasks which you will need to walk the user through with the compassionate heart of a teacher and using easily understandable language. You tasks are:" 
# put master prompt here

# Ensure Ollama instance is running and accessible at oll_path
# if not os.path.exists(oll_path):
#    raise ValueError(f"Ollama instance not found at: {oll_path}")


# Define agent themes (adjust as needed)
themes = ["analytical", "empowering regenerative farming", "cautiously and watchful pest management"]


def get_user_prompt():
    # Prompts user for input and validates it.
    while True:
        prompt = input("Enter your prompt: ")
        if prompt:
            return prompt
        else:
            print("Please enter a prompt.")


def generate_agent_prompts(user_prompt, themes):
    #Duplicates the user prompt with different thematic twists.
    synth_agent_prompts = []
    for theme in themes:
        synth_agent_prompts.append(f"""As an advanced language model you should create 4 challenging and unique prompts for the task outlined below.
These samples should be intricately designed to test the limits of the Task Theme and Naive Prompt, challenging yet relevant to the task description. The prompts should be only one sentance long, each.

The task description and instruction is phrased as a generative task. The results prompts samples should be input to the the model.
The model will be able then to generate an example given the instructions and the prompt input.
Task Theme:
{theme.capitalize()}
Naive Prompt:
{user_prompt}""")
    return synth_agent_prompts

def generate_agent_prompts(synth_agent_prompts, master_prompt):
    #Duplicates the user prompt with different thematic twists.
    agent_prompts = []
    for synth_agent_prompt in synth_agent_prompts:
        agent_prompts.append(f"{master_prompt}: {synth_agent_prompt}")
    return agent_prompts


def call_ollama(prompt):
    #Calls the Ollama LLM and returns its output.
    oll_pipeline = pipeline("text-generation", model=f"{oll_path}")
    return oll_pipeline(prompt, max_length=1024, top_k=1, do_sample=True)[0]["generated_text"]


def main():
    #Main execution flow.
    user_prompt = get_user_prompt()
    agent_prompts = generate_agent_prompts(user_prompt, themes)

    # Call Ollama for each agent prompt and concatenate outputs
    final_output = ""
    for prompt in agent_prompts:
        agent_output = call_ollama(prompt)
        final_output += f"\n**{prompt}**\n{agent_output}\n"

    # Create unique filename and save output
    filename = f"output_{int(time.time())}.txt"
    with open(os.path.join(output_folder, filename), "w") as f:
        f.write(final_output)

    print(f"Output saved to: {os.path.join(output_folder, filename)}")


if __name__ == "__main__":
    main()
