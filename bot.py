import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from google import genai

logging.basicConfig(level=logging.INFO)

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

ai = genai.Client(api_key=GEMINI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Saya OXYFANN AI 🤖\nSilakan kirim pertanyaan."
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text

    try:
        response = ai.models.generate_content(
            model="gemini-3.8-flash",
            contents=question
        )
        answer = response.text or "Maaf, AI belum menghasilkan jawaban."
        await update.message.reply_text(answer[:4000])

    except Exception:
        logging.exception("AI request failed")
        await update.message.reply_text(
            "Maaf, AI sedang mengalami kendala. Coba lagi nanti."
        )

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("OXYFANN AI Agent berjalan!")
    app.run_polling()

if __name__ == "__main__":
    main()
