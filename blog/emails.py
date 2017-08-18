# from django.conf import settings
# from django.core.mail import EmailMessage
# from django.template import Context
# from django.template.loader import render_to_string


# def send_feedback_email(email, message):
#     c = Context({'email': email, 'message': message})

#     email_subject = "Thank You"
#     email_body = "This is a test email that is used to test if the task manager is working"

#     email = EmailMessage(
#         email_subject, email_body, email,
#         [settings.DEFAULT_FROM_EMAIL], [],
#         headers={'Reply-To': email}
#     )
#     return email.send(fail_silently=False)


from django.core.mail import send_mail

def send_feedback_email(name,email,message):
    send_mail(name,message+" \n "+email,email,['recepients email'],fail_silently=False)