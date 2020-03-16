from django.conf import settings
from django.core.mail import send_mail


def send_email(subject, message, emails, html_message, from_email=settings.EMAIL_HOST_USER):
    return send_mail(subject, message, from_email, emails, fail_silently=False, html_message=html_message)
