import smtplib
import ssl
import datetime
import time
import imaplib
import email

reply_subject_template = "Re: {original_subject}"
reply_content = """Hello {sender_name},

Thank you for your email. Please note that I have received your message and will get back to you on the first working day after weekend.

Best regards,
Emaz"""

imap_server = 'imap.gmail.com'
imap_port = 993
imap_username = 'your_email@gmail.com'
imap_password = 'your_password'

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_password'

# Get current date and time
current_date = datetime.datetime.now()

# Connect to the IMAP server
imap_server_connection = imaplib.IMAP4_SSL(imap_server, imap_port)
imap_server_connection.login(imap_username, imap_password)
imap_server_connection.select("INBOX")

# Connect to the SMTP server
smtp_context = ssl.create_default_context()
smtp_server_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_server_connection.starttls(context=smtp_context)
smtp_server_connection.login(smtp_username, smtp_password)

while True:
    # Check if it is the weekend
    if current_date.weekday() in [5, 6]:
        # Check for new emails
        status, response = imap_server_connection.search(None, "UNSEEN")
        email_ids = response[0].split()
        if email_ids:
            for email_id in email_ids:
                _, email_data = imap_server_connection.fetch(email_id, "(RFC822)")
                raw_email = email_data[0][1]
                email_message = email.message_from_bytes(raw_email)

                original_subject = email_message['Subject']
                sender_name = email.utils.parseaddr(email_message['From'])[0]

                # Compose the reply email
                reply_subject = reply_subject_template.format(original_subject=original_subject)
                reply_body = reply_content.format(sender_name=sender_name)

                # Construct the email message
                message = f"Subject: {reply_subject}\n\n{reply_body}"

                # Send the reply email
                smtp_server_connection.sendmail(smtp_username, email_message['From'], message)

            print(f"{len(email_ids)} new email(s) replied to.")

    # Wait for some time before checking for new emails again (1000 seconds)
    time.sleep(1000)

    # Update the current date and time
    current_date = datetime.datetime.now()

imap_server_connection.close()
imap_server_connection.logout()
smtp_server_connection.quit()

