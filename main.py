import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your email', 'your password')
    email = EmailMessage()
    email['From'] = 'your email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

# email dictionary
email_list = {
    'demo key1': 'demo value1',
    'demo key2': 'demo value2'
}


def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('what is the subject of your email')
    subject = get_info()
    talk('tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('hey your email is sent')
    talk('do you want to send more?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
