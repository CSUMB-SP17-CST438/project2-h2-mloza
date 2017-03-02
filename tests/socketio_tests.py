import unittest
# import sys
# sys.path.insert(0, '/proj2-h2/app.py')
import app

class SocketIOTests(unittest.TestCase):
    def test_on_connect(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        # print r
        server_msg = r[0]
        self.assertEqual(server_msg['name'], 'allchats')
        # print server_msg
        
        
    def test_on_disconnect(self):
        client = app.socketio.test_client(app.app)
        r = client.disconnect()
        self.assertEqual(r, None)
        
        
    # def test_fbDisconnection(self):
    #     client = app.socketio.test_client(app.app)
    #     r = client.get_received()
    #     # print r
    #     server_msg = r[1]
    #     # print server_msg
    #     self.assertEquals(server_msg['name'], 'allusers')
        
    def test_gDisconnection(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        # print r
        server_msg = r[1]
        # print server_msg
        self.assertEquals(server_msg['name'], 'allusers')
        
    def test_on_new_chat(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        # print r
        server_msg = r[0]
        # print server_msg
        self.assertEquals(server_msg['name'], 'allchats')
        
    def test_on_new_chat_google(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        # print r
        server_msg = r[0]
        # print server_msg
        self.assertEquals(server_msg['name'], 'allchats')
        
        
if __name__ == '__main__':
    unittest.main()