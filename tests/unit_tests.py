import unittest
import requests
from urlparse import urlparse
# import testFunctions


# ------------------------------- functions ---------------------------------------
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
        
def get_rawr_command(msg):
    if msg == '!! rawr':
        return "rawr found"
    else:
        return "rawr not found"
        
def get_eat_command(msg):
    if msg == '!! eat':
        return "eat found"
    else:
        return "eat not found"
        
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
            
def split(msg):
    arr = []
    t = msg[8:]
    arr = t.split(' ', 1)
    return arr
# ---------------------------------------------------------------------------------

    

# --------------------------------- unit tests ------------------------------------
class ChatbotResponseTest(unittest.TestCase):
    def test_possible_chatbot_command(self):
        r = get_chatbot_reponse('!! sushi')
        self.assertEqual('active', r)
        
    def test_specific_command(self):
        r = get_specific_command('!! about')
        self.assertEqual('found', r)
        
    def test_say_command(self):
        r = get_say_command('!! say hi')
        self.assertEqual('say found', r)
    
    def test_about_command(self):
        r = get_about_command('!! about')
        self.assertEqual('about found', r)
        
    def test_help_command(self):
        r = get_help_command('!! help')
        self.assertEqual('help found', r)
        
    def test_rawr_command(self):
        r = get_rawr_command('!! rawr')
        self.assertEqual('rawr found', r)
        
    def test_eat_command(self):
        r = get_eat_command('!! eat')
        self.assertEqual('eat found', r)
        
        
class UrlTest(unittest.TestCase):
    def test_valid_url(self):
        r = get_url('http://www.google.com')
        self.assertEqual('valid', r)
        
    def test_valid_img(self):
        r = get_image('https://media.giphy.com/media/X2QBmjCQAHtle/giphy.gif')
        self.assertEqual('valid', r)
        
class SplittingText(unittest.TestCase):
    def test_splitting(self):
        r = split('sushi Seaside, CA')
        self.assertEqual(2, len(r))
# ---------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
    
    
    
