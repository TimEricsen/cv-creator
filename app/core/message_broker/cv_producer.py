import pika
import os, json

from dotenv import load_dotenv
from pika.adapters.blocking_connection import BlockingChannel

load_dotenv()


class CVProducer:
    def __init__(self):
        url = os.getenv('AMQP_URL')
        params = pika.URLParameters(url)
        self.__connection = pika.BlockingConnection(params)

    def __create_channel(self) -> BlockingChannel:
        channel = self.__connection.channel()
        return channel

    async def __create_exchange_queue(self) -> None:
        channel = self.__create_channel()
        channel.exchange_declare(
            exchange=os.getenv('EXCHANGE'), exchange_type=os.getenv('EXCHANGE_TYPE')
        )

        channel.queue_declare(
            queue=os.getenv('QUEUE')
        )
        channel.queue_bind(
            queue=os.getenv('QUEUE'),
            exchange=os.getenv('EXCHANGE'),
            routing_key=os.getenv('ROUTING_KEY')
        )

    async def publish_message(self, message_body) -> None:
        await self.__create_exchange_queue()
        channel = self.__create_channel()
        channel.basic_publish(
            exchange=os.getenv('EXCHANGE'),
            routing_key=os.getenv('ROUTING_KEY'),
            body=json.dumps(message_body)
        )
        self.__connection.close()


def get_cv_producer() -> CVProducer:
    return CVProducer()
