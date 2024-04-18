# answer.py
import logging
import os

from flask import abort

from llm.answer import just_answer, chat as llm_chat, new_chat as llm_new_chat, rephrase_web, answer_using_context
from llm.moderate import moderations
from serpapi import GoogleSearch

logger = logging.getLogger(__name__)


def search(question):
    """
    Search web and return URL.

    :param question:
    :return:
    """
    to_answer = question.get("question")
    if moderations(to_answer):
        abort(406, "You ask bad question, I will not answer that.")
    q = rephrase_web(to_answer)

    params = {
        "engine": "google",
        "q": q,
        "api_key": os.environ["SERP_API_KEY"],
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]
    context = []
    for data in organic_results:
        if data.get("missing", None) is None:
            continue
        context.append(
            dict(title=data["title"], url=data["link"], description=data["snippet"], date=data.get("date", "Unknown"))
        )

    logger.info(organic_results)
    ret = answer_using_context(q, context)
    return dict(reply=ret), 200


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
