import unittest
import requests

class SeleniumTest(unittest.TestCase):

    def test_get_request(self):
        # Setup
        url = 'http://localhost:8080/'
        # Exercise
        req = requests.get(url = url)
        # Verify
        response = req.text
        print(f"Response: {response}")


    def test_post_request(self):
        # Setup
        url = 'http://localhost:8080/translator'    
        data = {'word':'cat',
                'language':'Deutsch',
                'action': 'Translate'}
        # Exercise
        req = requests.post(url = url, data = data)
        # Verify
        response = req.text
        print(f"Response: {response}")
        self.assertTrue('Translate: cat into Katze' in response)
        # Teardown

if __name__ == '__main__':
    unittest.main()
