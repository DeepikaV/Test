import smtplib
import imaplib
from email.mime.text import MIMEText

class myFunctions2:
    def send_email(self, destination, subject, message):

        username = 'paqatester01@gmail.com'
        password = '550College'

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = destination

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(username, destination, msg.as_string())
        server.quit()

    def search_email(self, *args):

        username = 'paqatester01@gmail.com'
        password = '550College'
        
        mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
        mailbox.login(username, password)
        mailbox.select('Inbox')
        item = mailbox.search(None, *args)
        mailbox.close()
        mailbox.logout()
        if item[0] == 'OK':
            if item[1] == ['']:
                raise AssertionError("No mail found!")
            else:
                return item[1][0].split()
        elif item[0] == 'NO':
            raise AssertionError("I don't understand your search query!")
        else:
            raise AssertionError("Mail server error!")

    def delete_email(self, messageID):
        
        username = 'paqatester01@gmail.com'
        password = '550College'
        
        mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
        mailbox.login(username, password)
        mailbox.select('Inbox')
        for index in messageID :
            mailbox.store(index, '+FLAGS', '\\Deleted')
        mailbox.expunge()
        mailbox.close()
        mailbox.logout()
