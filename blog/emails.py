from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.template import Context, Template
from django.template.loader import render_to_string


EMAIL_TEMPLATE = """
This is a sample email that is just used for testing

Does it wor, well i don't know
"""

def send_feedback_email():
    template = Template(EMAIL_TEMPLATE)
    send_mail(
        "Blog Site Test Subject",
        template.render(),
        "khalifsteve16@gmail.com",
        ["stephenkanyi7@gmail.com"],
        fail_silently=False,
    )
    