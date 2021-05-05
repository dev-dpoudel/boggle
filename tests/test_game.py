import unittest
import requests


class TestBoggle(unittest.TestCase):

    baseurl = "http://localhost:8000/{}"

    def test_board(self):
        url = self.baseurl.format("keys")
        response = requests.get(url)
        data = response.json()
        board = data["keys"]
        # Test the size of the Board. It must be 4 * 4
        self.assertEquals(len(board), 16, "Board must be 4*4")

    def test_isValid_word(self):
        url = self.baseurl.format("list")
        response = requests.get(url)
        data = response.json()
        print(response.text)
        words = data["words"]
        # Test the size of the Board. It must be 4 * 4
        self.assertEquals(len(words), 0, "No words found")
        print(words, "Test")
        # Test Word is valid
        query = "valid?word=%s" % (words[0])
        url = self.baseurl.format(query)
        response = requests.get(url)
        data = response.json()
        success = data["success"]
        # Check for Success
        self.assertTrue(success, "Word not matched")

    def test_inValid_word(self):
        # Test Word is In valid
        query = "/valid?word=%s" % ("RoughExampleTesting")
        url = self.baseurl.format(query)
        response = requests.get(url)
        data = response.json()
        success = data["success"]
        # Check for Success
        self.assertTrue(success, "Word is found")

    def test_get_score(self):
        query = "valid?word=%s" % ("RoughExampleTesting")
        url = self.baseurl.format(query)
        response = requests.get(url)
        data = response.json()
        success = data["success"]
        # Check for Success
        self.assertTrue(success, response.text)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBoggle('test_board'))
    suite.addTest(TestBoggle('test_isValid_word'))
    # suite.addTest(TestBoggle('test_inValid_word'))
    # suite.addTest(TestBoggle('test_get_score'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
