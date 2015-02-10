import unittest
from nxci.tasks import give_me_three, give_me_five

class NxCi(unittest.TestCase):

    def test_give_me_three(self):
        self.assertEqual(give_me_three(), 3)

    def test_give_me_five(self):
        self.assertEqual(give_me_five(),5)

    def test_more_tests(self):
        self.assertEqual(5,5)

    def test_more_tests(self):
        self.assertEqual(2,2)

    def test_more_tests(self):
        self.assertEqual(1,2)

if __name__ == '__main__':
    unittest.main()
