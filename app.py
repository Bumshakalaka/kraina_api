# app.py
import logging
from dotenv import load_dotenv, find_dotenv

from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    logger = logging.getLogger(__name__)
    loggerFormat = "%(asctime)s:\t%(message)s"
    loggerFormatter = logging.Formatter(loggerFormat)
    loggerLevel = logging.INFO
    logging.basicConfig(format=loggerFormat, level=loggerLevel)
    app.run(host="0.0.0.0", port=8000, log_level="debug")
