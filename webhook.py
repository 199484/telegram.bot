import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_TOKEN")

app = Flask(__name__)

# --- Telegram bot logic ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я живий 🤖 і працюю через webhook!")

telegram_app = Application.builder().token(TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))


@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    telegram_app.update_queue.put_nowait(update)
    return "ok"


@app.route("/", methods=["GET"])
def index():
    return "Bot is alive 🚀"


if __name__ == "__main__":
    telegram_app.initialize()
    telegram_app.start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
