# answer.py
import logging

from flask import abort

from llm.answer import just_answer, chat as llm_chat, new_chat as llm_new_chat
from llm.moderate import moderations

logger = logging.getLogger(__name__)


def answer(question):
    """
    Answer a question using LLM, no history chat.

    :param question:
    :return:
    """
    to_answer = question.get("question")
    if moderations(to_answer):
        abort(406, "You ask bad question, I will not answer that.")
    reply = just_answer(to_answer)
    return dict(reply=reply), 200


def chat(question):
    """
    Answer a questions in chat mode.

    All human and AI messages are remembered in sqlite db under new chat session id
    :param question:
    :return:
    """
    to_answer = question.get("question")
    if moderations(to_answer):
        abort(406, "You ask bad question, I will not answer that.")
    reply = llm_chat(to_answer)
    return dict(reply=reply), 200


def new_chat():
    """
    Create a new chat.

    :return:
    """
    return llm_new_chat(), 200


def new_chat_ext(chat_settings):
    """
    Create a new chat.

    :return:
    """
    settings = dict(chat_settings)
    return llm_new_chat(settings), 200
