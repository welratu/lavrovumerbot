import re

from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8062489806:AAFSWWiJGU3gglcLope0LdYhqRGbMR3Y6VM"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if re.search(r"\bлавров(?:а|у)?\b", text):
        await update.message.reply_text("царствие ему небесное")

    elif re.search(
        r"\b(?:"
        r"завр(?:а|у|ом|е|ы|ов|ам|ами|ах)?|"
        r"приваленко|"
        r"стас(?:а|у|ом|е)?|"
        r"привалов(?:а|у|ым|е)?"
        r")\b",
        text,
    ):
        await update.message.reply_text(
            "завр приваленко виддав життя за украину и його йобнуло шахидом 🕯️🕯️🥀 царствие йому небесное"
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    app.run_polling()


if __name__ == "__main__":
    main()
