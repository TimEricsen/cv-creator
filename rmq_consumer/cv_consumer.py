import os, pika

from typing import Callable
from dotenv import load_dotenv
from pika.adapters.blocking_connection import BlockingChannel


load_dotenv()


class CVConsumer:
    def __init__(self):
        url = os.getenv('AMQP_URL')
        params = pika.URLParameters(url)
        self.__connection = pika.BlockingConnection(params)

    def __create_channel(self) -> BlockingChannel:
        channel = self.__connection.channel()
        return channel

    def __create_queue(self) -> None:
        channel = self.__create_channel()
        channel.queue_declare(queue=os.getenv('QUEUE'))

    def consume_message(self, callback: Callable) -> None:
        self.__create_queue()
        channel = self.__create_channel()
        channel.basic_consume(
            queue=os.getenv('QUEUE'),
            on_message_callback=callback,
            auto_ack=True
        )
        channel.start_consuming()
        self.__connection.close()


def get_cv_consumer() -> CVConsumer:
    return CVConsumer()
