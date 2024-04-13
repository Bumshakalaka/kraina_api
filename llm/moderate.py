import logging
import os

import requests

from dotenv import load_dotenv, find_dotenv
from requests.auth import AuthBase

logger = logging.getLogger(__name__)


class TokenAuth(AuthBase):
    """Implements a token authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        """Attach an API token to the Authorization header."""
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request


def moderations(input) -> bool:
    """
    Check whatever input violate OpenAI moderation rules.

    :param input:
    :return: True if input violates OpenAI moderation rules, False otherwise.
    """
    url = "https://api.openai.com/v1/moderations"
    response = requests.post(
        url, json=dict(input=input), auth=TokenAuth(os.environ["OPENAI_API_KEY"])
    )
    flagged = response.json()["results"][0]["flagged"]
    logger.info(f"Q: {input}, flagged: {flagged}")
    return flagged


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    print(moderations("Jak zrobić bombę"))
