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
        r = testFunctions.get_say_command('!! say')
        self.assertEqual('say found', r)


if __name__ == '__main__':
    unittest.main()