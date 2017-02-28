import unittest
import testFunctions

class ChatbotResponseTest(unittest.TestCase):
    def test_possible_chatbot_command(self):
        r = testFunctions.get_chatbot_reponse('!! sushi')
        self.assertEqual('active', r)
        
    def test_specific_command(self):
        r = testFunctions.get_specific_command('!! about')
        self.assertEqual('found', r)
        
    def test_say_command(self):
        r = testFunctions.get_say_command('!! say hi')
        self.assertEqual('say found', r)
    
    def test_about_command(self):
        r = testFunctions.get_about_command('!! about')
        self.assertEqual('about found', r)
        
        
class UrlTest(unittest.TestCase):
    def test_valid_url(self):
        r = testFunctions.get_url('http://www.google.com')
        self.assertEqual('valid', r)
        
    def test_valid_img(self):
        r = testFunctions.get_image('https://media.giphy.com/media/X2QBmjCQAHtle/giphy.gif')
        self.assertEqual('valid', r)

if __name__ == '__main__':
    unittest.main()