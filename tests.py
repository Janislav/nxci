import unittest
from nxci.tasks import give_me_three

class NxCi(unittest.TestCase):

    def test_give_me_three(self):
        self.assertEqual(give_me_three(), 3)

if __name__ == '__main__':
    unittest.main()
