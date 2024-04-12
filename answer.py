# answer.py

from flask import abort, make_response

from llm.answer import answer_consist
from llm.moderate import Moderate


async def answer(question):
    to_answer = question.get("question")
    if Moderate().moderations(to_answer):
        abort(406, "You ask bad question, I will not answer that.")
    reply = answer_consist(to_answer)
    return dict(reply=reply), 200
