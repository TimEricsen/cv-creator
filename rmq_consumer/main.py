import json

from rmq_consumer.cv_consumer import get_cv_consumer
from rmq_consumer.pdf_creator import PDFCreator
from rmq_consumer.send_email import get_email_sender


def callback(ch, method, properties, body):
    body = json.loads(body)
    file = PDFCreator(body)
    file.create_cv()
    email_send = get_email_sender(body)
    email_send.send_email()


def main():
    consumer = get_cv_consumer()
    consumer.consume_message(callback=callback)


if __name__ == '__main__':
    main()
