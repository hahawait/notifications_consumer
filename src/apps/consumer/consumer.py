import json
from apps.consumer.connection import RabbitMQConnection

class RabbitMQFacade:
    def __init__(self, queue_name: str, connection: RabbitMQConnection) -> None:
        self.queue_name = queue_name
        self.connection = connection

    async def consume_messages(self, callback):
        connection = await self.connection.connect()
        async with connection:
            channel = await connection.channel()
            await channel.set_qos(prefetch_count=1)
            queue = await channel.declare_queue(self.queue_name, durable=True)

            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        data = json.loads(message.body)
                        await callback(data)