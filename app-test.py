from app import app
import unittest

class BaseAppTestCase(unittest.TestCase):
    def test_initial(self):
        testinit = app.test_client(self)
        response = testinit.get('/', content_type='html/text')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data , b'Hello TDD')

if __name__ == '__main__':
    unittest.main()
