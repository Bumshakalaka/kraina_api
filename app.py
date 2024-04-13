# app.py
import argparse
import logging
import sys

from dotenv import load_dotenv, find_dotenv

from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def home():
    """
    Home page.

    :return:
    """
    return render_template("home.html")


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    logger = logging.getLogger(__name__)
    loggerFormat = "%(asctime)s [%(levelname)8s] [%(name)32s]: %(message)s"
    loggerFormatter = logging.Formatter(loggerFormat)
    loggerLevel = logging.INFO
    file_handler = logging.FileHandler("app.log")
    console_handler = logging.StreamHandler(sys.stdout)
    logging.basicConfig(
        format=loggerFormat, level=loggerLevel, handlers=[file_handler, console_handler]
    )
    parser = argparse.ArgumentParser(description="Run krAIna API server")
    parser.add_argument(
        "--host",
        required=False,
        default="0.0.0.0",
        help="Server host IP, default 0.0.0.0",
    )
    parser.add_argument(
        "--port", required=False, default=8000, help="Server port, default 8000"
    )
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, log_config=None)
