from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8062489806:AAFSWWiJGU3gglcLope0LdYhqRGbMR3Y6VM"

TRIGGERS = {
    "лавров",
    "лаврова",
    "лаврову",
}

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower().strip()

    if text in TRIGGERS:
        await update.message.reply_text("царствие ему небесное")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    app.run_polling()

if __name__ == "__main__":
    main()