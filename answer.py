# answer.py
import logging

from flask import abort

from llm.answer import answer_consist, chat as llm_chat, new_chat as llm_new_chat
from llm.moderate import Moderate

logger = logging.getLogger(__name__)


def answer(question):
    to_answer = question.get("question")
    if Moderate().moderations(to_answer):
        abort(406, "You ask bad question, I will not answer that.")
    reply = answer_consist(to_answer)
    return dict(reply=reply), 200


def chat(question):
    to_answer = question.get("question")
    if Moderate().moderations(to_answer):
        abort(406, "You ask bad question, I will not answer that.")
    reply = llm_chat(to_answer)
    return dict(reply=reply), 200


def new_chat():
    return dict(session_id=llm_new_chat()), 200
