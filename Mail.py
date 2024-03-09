'''import smtplib, ssl
from email.message import EmailMessage
def mail():
        port=465  # For SSL
        smtp_server="smtp.gmail.com"
        sender_email="donorlanemi@gmail.com"  # Enter your address
        receiver_email="ishisinghal0304@gmail.com"  # Enter receiver address
        password = "neunxpepmbjsjupq"

        msg = EmailMessage()
        msg.set_content("Thankyou for participating in this Noble Cause!")
        msg['Subject'] = "Appreciation Certificate!"
        msg['From'] = sender_email
        msg['To'] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
            print("Email Sent")
mail()'''


def mail():
    import yagmail
    from_ = 'donorlanemi@gmail.com'
    password = 'kmqfmoyfzczphztd'  # set this
    receiver = 'ishisinghal0304@gmail.com'
    body = 'Thankyou for helping in this noble cause!'
    filename = r'C:\Users\User\Desktop\donorlane certificate.pdf'  # this file path should be given correctly
    yag = yagmail.SMTP(from_, password)
    yag.send(
        to=receiver,
        subject="text email",
        contents=body,
        attachments=filename)
    print("mail sent")
mail()