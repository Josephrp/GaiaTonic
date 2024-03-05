from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

assistant = AssistantAgent(
    name="chatbot",
    system_message="""You are an assistant.
        The user will ask a question.
        You may use the provided functions before providing a final answer.
        Only use the functions you were provided.
        When the answer has been provided, reply TERMINATE.""",
    llm_config=llm_config,
)

user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config=False,
    is_termination_msg=_is_termination_msg,
    default_auto_reply="Reply TERMINATE when the initial request has been fulfilled.",
    human_input_mode="NEVER",
)


user_proxy.register_function(
    function_map={
        "define_function": define_function
    }
)
