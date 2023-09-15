import smtplib, ssl, os

from email.message import EmailMessage
from dotenv import load_dotenv


class EmailSender:
    def __init__(self, data: dict):
        self.data = data

    def send_email(self):
        context = self.__set_context()
        content = self.__get_content()
        msg = self.__get_message()
        with smtplib.SMTP_SSL(content['server'], content['port'], context=context) as server:
            server.login(content['sender'], content['password'])
            server.sendmail(content['sender'], self.data['email'], msg.as_string())

    def __set_context(self) -> ssl.SSLContext:
        return ssl.create_default_context()

    def __get_content(self) -> dict:
        load_dotenv()
        content = dict()
        content['server'] = os.getenv('SMTP_SERVER')
        content['port'] = os.getenv('PORT')
        content['sender'] = os.getenv('EMAIL_SENDER')
        content['password'] = os.getenv('EMAIL_PASSWORD')
        return content

    def __get_message(self) -> EmailMessage:
        content = self.__get_content()
        msg = EmailMessage()
        msg['Subject'] = 'Your CV'
        msg['From'] = f'me {content["sender"]}'
        msg['To'] = f'recipient {self.data["email"]}'

        msg.set_content('Hello! There is your CV! Thank you for using our platform!'
                        ' Hope you will find job as fast as possible! Good luck!')
        with open(f'{self.data["full_name"].replace(" ", "")}.pdf', mode='rb') as file:
            msg.add_attachment(file.read(), "application", "pdf")
        return msg


def get_email_sender(data: dict) -> EmailSender:
    return EmailSender(data)
