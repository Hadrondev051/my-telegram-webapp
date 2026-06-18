from flask import Flask, request
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests
import os

TOKEN = "توکن_ربات_اینجا"  # از @BotFather بگیر
WEBAPP_URL = "https://your-username.github.io/repo-name"  # بعداً عوض میشه

app = Flask(__name__)
bot_app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("🚀 باز کردن وب‌اپ", web_app=WebAppInfo(WEBAPP_URL))]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("👋 سلام! روی دکمه زیر بزن تا وب‌اپ باز بشه:", reply_markup=reply_markup)

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    await update.message.reply_text(f"📩 داده دریافت شد: {data}")

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.process_update(update)
    return "OK", 200

@app.route("/")
def index():
    return "ربات فعال است ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)