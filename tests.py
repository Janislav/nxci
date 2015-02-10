import unittest
from nxci.tasks import give_me_three, give_me_five, give_me_seven

class NxCi(unittest.TestCase):

    def test_give_me_three(self):
        self.assertEqual(give_me_three(), 3)

    def test_give_me_five(self):
        self.assertEqual(give_me_five(),5)

    def test_give_me_seven(self):
        self.assertEqual(7, give_me_seven())

if __name__ == '__main__':
    unittest.main()
