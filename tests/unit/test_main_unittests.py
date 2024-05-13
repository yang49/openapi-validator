import unittest

class TestMain(unittest.TestCase):

    def test_main(self):
        print("Test Main")
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main() 