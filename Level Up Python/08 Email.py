import smtplib

SENDER_EMAIL = 'masoom.reza@teva.co.in'
SENDER_PASSWORD = 'Lala@2786'

def send_email(receiver_email, subject, body):
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

send_email('masoom.reza@teva.co.in', 'Notifcation', 'Test')