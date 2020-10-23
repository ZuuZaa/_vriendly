import random 
import string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def generate_token(size=120, chars=string.ascii_letters + string.digits):
    token = "".join([random.choice(chars) for _ in range(size) ])
    return token

def send_verification_mail(email, link):
    print('---------',settings.EMAIL_HOST_USER)
    subject, from_email, to = 'Confirm your email address.', settings.EMAIL_HOST_USER, email
    print('---------', to)
    text_content = 'Confirm your email address.'
    html_content = f'<p>Click this <a href="{link}">link</a> for verification.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    print('------ message', msg)
    msg.send()


