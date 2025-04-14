import smtplib

# Debug mode enable karna
server = smtplib.SMTP("smtp-relay.brevo.com", 587)
server.set_debuglevel(1)  # SMTP Debugging ON
server.starttls()  # Secure connection start karna

# SMTP Login
server.login("87d637001@smtp-brevo.com", "csZLtAx9wCdby1DQ")

# Email Send Karna
from_email = "neuralnitin@gmail.com"
to_email = "nitinnegi22194@gmail.com"
subject = "Test Email from Python"
message = f"Subject: {subject}\n\nThis is a test email."

server.sendmail(from_email, to_email, message)
server.quit()

