import unittest
import requests


class TestBoggle(unittest.TestCase):

    baseurl = "http://localhost:8000/{}"

    headers = {'cookie': 'session=.eJxNj7EKwzAMRP_Fc76gmwgBbQILaouSIa2XLA2khVJK_73SOUOHk4V9ejp_0nVb9pZOl2RpSOQa_86zq7rUlV3FxS5x2fE2wT8Pqa2357rdl_0dOOEYKhxWyYBRVCVDjd4oYGPGDQcoU0wxPCPFSpYJBEJv8CAqmCqIRxVTiJIVtPBnI_TS0bVDFTzF_thAykga3oIsPBVYkeuI11eDRNZDCqw1_v7a9vbwb8_fH62oTdk.YJH2-A.qu5BaGdRLezjtQLV6j2po9IqHVU'}

    def test_board(self):
        url = self.baseurl.format("keys")
        response = requests.get(url)
        data = response.json()
        board = data["keys"]
        # Test the size of the Board. It must be 4 * 4
        self.assertEquals(len(board), 16, "Board must be 4*4")

    def test_isValid_word(self):
        url = self.baseurl.format("list")
        response = requests.get(url, headers=self.headers)
        data = response.json()
        words = data["words"]
        # Test the size of the Board. It must be 4 * 4
        self.assertNotEqual(len(words), 0, "No words found")
        # Test Word is valid
        query = "valid?word=%s" % (words[0])
        url = self.baseurl.format(query)
        response = requests.put(url, headers=self.headers)
        data = response.json()
        success = data["success"]
        # Check for Success
        self.assertTrue(success, "Word not matched")

    def test_inValid_word(self):
        # Test Word is In valid
        query = "/valid?word=%s" % ("RoughExampleTesting")
        url = self.baseurl.format(query)
        response = requests.put(url, headers=self.headers)
        data = response.json()
        success = data["success"]
        # Check for Success
        self.assertFalse(success, "Word is found")

    def test_get_score(self):
        query = "results"
        url = self.baseurl.format(query)
        response = requests.get(url, headers=self.headers)
        data = response.json()
        results = data["results"]
        assert results is not None


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBoggle('test_board'))
    suite.addTest(TestBoggle('test_isValid_word'))
    suite.addTest(TestBoggle('test_inValid_word'))
    suite.addTest(TestBoggle('test_get_score'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
