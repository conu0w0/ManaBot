# keep_alive.py
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "黑堂 真乃在線 ☕"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
