import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
password = "your_app_password"
receiver = "test@email.com"

subject = "AutoLead AI Outreach"

body = """
Hi,

We discovered your business online while researching makeup studios in Delhi.

We would love to connect and collaborate.

Best regards,
AutoLead AI
"""

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)
server.send_message(msg)

server.quit()

print("Email sent successfully")