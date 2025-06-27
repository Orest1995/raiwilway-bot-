
from flask import Flask
from threading import Thread
import os

web_app = Flask("")

@web_app.route("/")
def home():
    return "Бот живий!"

def run():
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()
