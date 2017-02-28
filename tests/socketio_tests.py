import unittest
import sys
sys.path.insert(0, '/proj2-h2/app.py')
import app

class SocketIOTests(unittest.TestCase):
    def tset_on_connect(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        server_msg = r[0]
        self.assertEqual(server_msg['name'], 'allchats')
        print server_msg
        
        
        
if __name__ == '__main__':
    unittest.main()