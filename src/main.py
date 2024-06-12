import asyncio
import logging
from aiogram import Bot

from logger.logger import init_logger
from settings import get_config

from apps.bot.handlers import send_unread_messages
from apps.consumer.consumer import RabbitMQFacade
from apps.consumer.connection import RabbitMQConnection

async def main():
    init_logger("INFO")
    config = get_config()

    connection = RabbitMQConnection(config.consumer_settings)
    facade = RabbitMQFacade(config.consumer_settings.QUEUE_NAME, connection)

    async with Bot(token=config.bot_settings.BOT_TOKEN) as bot:
        async def process_message(data):
            await send_unread_messages(bot, data)

        await facade.consume_messages(process_message)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot was stopped!!!")