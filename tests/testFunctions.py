import requests
from urlparse import urlparse

def get_chatbot_reponse(msg):
    test = msg.find("!!", 0, 2)
    if (test != -1):
        return "active"
    else:
        return "deactive"
        
def get_specific_command(msg):
    about = msg.find("!! about", 0, 6)
    hlp = msg.find("!! help", 0, 6)
    rawr = msg.find("!! rawr", 0, 6)
    eat = msg.find("!! eat", 0, 6)
    say = msg.find("!! sat", 0, 6)
    if (about == -1) or (hlp == -1) or (rawr == -1) or (eat == -1) or (say == -1):
        return "found"
    else:
        return "unknown"
        
def get_say_command(msg):
    say = msg.find("!! say", 0, 6)
    if say != -1:
        return "say found"
    else:
        return "say not found"
        
def get_about_command(msg):
    if msg == '!! about':
        return "about found"
    else:
        return "about not found"
        
def get_help_command(msg):
    if msg == '!! help':
        return "help found"
    else:
        return "help not found"
        
def get_url(msg):
    test = urlparse(msg)
    if (test.scheme or test.netloc):
        return "valid"
    else:
        return "not valid"
        
def get_image(msg):
    if (get_url(msg) == 'valid'):
        image = requests.head(msg)
        img = image.headers.get('content-type')
        if (img == "image/gif" or img == "image/png" or img == "image/jpeg"):
            return "valid"
        else:
            return "not valid"

    