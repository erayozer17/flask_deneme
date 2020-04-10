from extensions import celery
from services.email import send_transactional_mail


@celery.task(name='send_transactional_mail_task')
def send_transactional_mail_task(subject, recipients, html_body):
    send_transactional_mail(subject, recipients, html_body)
