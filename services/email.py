from flask_mail import Message
from extensions import mail

def send_transactional_mail(subject, recipients, html_body):
    msg = Message(subject, recipients=[recipients])
    msg.html = html_body
    mail.send(msg)
