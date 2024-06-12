import aio_pika
import logging
from settings import ConsumerSettings

class RabbitMQConnection:
    _instance = None
    _connection = None
    _logger = logging.getLogger("RabbitMQConnection")

    def __new__(cls, settings: ConsumerSettings) -> "RabbitMQConnection":
        if cls._instance is None:
            cls._instance = super(RabbitMQConnection, cls).__new__(cls)
            cls._settings = settings
            cls._logger.info("RabbitMQConnection instance created")
        return cls._instance

    @classmethod
    async def connect(cls):
        if cls._connection is None:
            cls._connection = await aio_pika.connect_robust(
                host=cls._settings.CONSUMER_HOST,
                port=cls._settings.CONSUMER_PORT,
                virtualhost=cls._settings.VIRTUAL_HOST,
                login=cls._settings.CONSUMER_USERNAME,
                password=cls._settings.CONSUMER_PASSWORD
            )
            cls._logger.info("RabbitMQ connection established")
        return cls._connection

    @classmethod
    async def close(cls):
        if cls._connection is not None:
            await cls._connection.close()
            cls._connection = None
            cls._logger.info("RabbitMQ connection closed")