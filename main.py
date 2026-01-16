import os
from flask import Flask
from threading import Thread
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive"

def run_web():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

def run_bot():
    while True:
        print("Bot is running...")
        time.sleep(60)

Thread(target=run_web).start()
Thread(target=run_bot).start()
