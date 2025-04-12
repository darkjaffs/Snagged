from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def init_mail(app):
    mail.init_app(app)
    
    
def send_email(to_email, jobs):
    subject = "Your curated job listings"
    body = "Here are the latest jobs in your selected category:\n\n"
    for job in jobs:
        body += f"• {job[0]} \n{job[1]}\nPosted on: {job[2]}\n\n"
        
    try:
        msg = Message(
            subject = subject,
            recipients = [to_email],
            body=body,
            sender = current_app.config['MAIL_USERNAME']
        )
        mail.send(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")

