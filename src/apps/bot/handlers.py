from aiogram import Bot

from apps.models import Message

async def send_unread_messages(bot: Bot, data):
    messages = [Message.model_validate_json(msg) for msg in data]
    message_text = "<b>Количество диалогов с непрочитанными сообщениями:</b> {}\n\n".format(len(messages))
    for message in messages:
        message_text += "<b>Диалог:</b> {}\n<b>Текст:</b> {}\n<b>Дата:</b> {}\n\n".format(
            message.dialog,
            message.text,
            message.datetime.strftime("%Y-%m-%d %H:%M:%S")
        )
    await bot.send_message(
        messages[0].user_id,
        text=message_text,
        parse_mode='HTML'
    )