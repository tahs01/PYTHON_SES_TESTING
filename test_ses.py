import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SES SMTP server details
smtp_server = 'email-smtp.region.amazonaws.com'  # Replace {region} with your AWS SES region
smtp_port = 25  # The port number for SMTP over TLS/SSL

# SES SMTP credentials
smtp_username = 'smtp_user_name'  # Replace with your SES SMTP username
smtp_password = 'smtp_user_password'  # Replace with your SES SMTP password 

# Sender and recipient email addresses
sender = 'sender@mail.com'
recipient = 'recepient@mail.com'

# Email message
subject = 'Test Email'
body = 'This is a test email sent via AWS SES SMTP by tahs.'

# Create a MIME multipart message
message = MIMEMultipart()
message['From'] = sender
message['To'] = recipient
message['Subject'] = subject

# Attach the email body
message.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SES SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption
    server.login(smtp_username, smtp_password)  # Login with SMTP credentials
    
    # Send the email
    server.sendmail(sender, recipient, message.as_string())
    print('Test email sent successfully.')

except Exception as e:
    print('An error occurred:', str(e))

finally:
    # Close the connection to the SMTP server
    server.quit()