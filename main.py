import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

server = smtplib.SMTP(config.smtp_address, config.smtp_port_no)
server.starttls()
server.login(config.email, config.password)

content = MIMEMultipart()
content["From"] = config.email
content["To"] = config.to_address
content["Subject"] = config.subject
content.attach(MIMEText(config.message))

server.send_message(content)