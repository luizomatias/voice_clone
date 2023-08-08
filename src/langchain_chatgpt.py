"""
chat_result function
"""
from dotenv import find_dotenv, load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv(find_dotenv(), override=True)


def chatgpt_result(system_message: str, human_message: str) -> str:
    """
    Initiate a conversation with the ChatGPT model using LangChain.

    Args:
        system_message (str): A system message to guide the model's behavior.
        human_message (str): The user's message to the chatbot.

    Returns:
        str: The model's response to the conversation as a string.
    """

    chatgpt = ChatOpenAI(model_name="gpt-3.5-turbo")

    result = chatgpt(
        [
            SystemMessage(content=system_message),
            HumanMessage(content=human_message),
        ],
        temperature=0,
        max_tokens=70,
    )

    return result.content
