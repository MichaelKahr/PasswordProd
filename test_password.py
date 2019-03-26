import unittest
from PasswordProducer import Password

class test_Password(unittest.TestCase):

    def test_check1(self):
        self.assertTrue( Password("sickshit").check("sickshit"))
        self.assertFalse( Password("sickshit").check("sickshit\n"))

if __name__ == '__main__':
    unittest.main()