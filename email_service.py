# Jaxon Terrell
# 8/2/20
# Program to send an email 
import smtplib
import ssl


def send_email():
    receiving_address = input("Type the receiving address of this email: ")
    sender = input("What is your email address: ")
    password = input("Type your email password: ")
    subject = input("What is the subject line: ")
    message = input("What is the message you'd like to send: ")
    formatted_message = 'Subject: {}\n\n{}'.format(subject, message)
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiving_address, formatted_message)


if __name__ == "__main__":
    send_email()