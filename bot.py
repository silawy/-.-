import os
from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.books import books_handler
from handlers.questions import question_handler

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(start_handler)
    app.add_handler(books_handler)
    app.add_handler(question_handler)
    app.run_polling()

if __name__ == "__main__":
    main()


---

📄 config.py

BOT_TOKEN = "8060215562:AAHwRrq8tPTMZdEl08UgylsuU5phLVVTOTg"
