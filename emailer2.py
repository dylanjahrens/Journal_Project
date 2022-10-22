
import question_gen
import datetime
import smtplib
import ssl
from email.message import EmailMessage

class Email():
    
    def __init__(self):
        self.recipients_list = ['dylanjahrens@gmail.com']
        self.sender_credentials = {'email': 'dylanjahrens@gmail.com',
                                'password': 'xxxxx'}
        '''
        create a new email, allow less secure apps, dual factor auth, and encrypt passoword
        with enviornment variable
        '''

    def send_email(self):
        self.question = question_gen.get_question()
        msg = EmailMessage()
        msg['Subject'] = 'Daily Gratitude'
        msg['From'] = self.sender_credentials['email']
        msg['To'] = ', '.join(self.recipients_list)
        #corey video at 28:00 , also explains HTML over plaintext
        text = f'''Daily Journal - {datetime.date.today().strftime("%A %B %d, %Y")}
        \n\nTake a few minutes to write or think and reflect on this:
        \n\n\n{self.question}'''

        '''
        if attaching a photo, Corey has a video at 18:00
        '''

        msg_body = text
        msg.set_content(msg_body) #configures plaintext

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(self.sender_credentials['email'],
                    self.sender_credentials['password'])
            server.send_message(msg)


if __name__ == '__main__':
    email = Email()
    email.send_email()
