import app
import unittest
import flask_testing
import requests
import urllib2


class ServerIntegrationTestCase(flask_testing.LiveServerTestCase):
    
    def create_app(self):
        return app.app

    def test_server_is_running(self):
        r = urllib2.urlopen(self.get_server_url())
        # print r
        self.assertEqual(r.code, 200)
        # self.assertEquals(r.text, 'Hello, world!')
        
    def test_server_render(self):
        r = requests.get(self.get_server_url()) 
        # print r.headers['content-type']
        self.assertEquals(r.headers['content-type'], 'text/html; charset=utf-8')
        # self.assert_template_used('index.html')



if __name__ == '__main__':
    unittest.main()