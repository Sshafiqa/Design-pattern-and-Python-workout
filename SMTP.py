import smtplib
from email.mime.text import MIMEText


def smtp_example(smtp_server, smtp_port, username, password, to_email, subject, body):
    try:
        # Create a text/plain message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = to_email

        # Connect to the SMTP server and send email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)
            server.sendmail(username, [to_email], msg.as_string())

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
smtp_example('smtp.example.com', 465, 'your_email@example.com', 'your_password', 'recipient@example.com', 'Subject',
             'Email body text')
