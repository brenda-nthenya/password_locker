import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Method that runs before each test method.
        '''
        self.new_user = User('Brenda', 'Qwerty')

    def test_init(self):
        '''
        Tests if the oject has correctly been initialized. 
        '''
        self.assertEqual(self.new_user.user_name, "Brenda")
        self.assertEqual(self.new_user.password, "Qwerty")


         
    

if __name__ == '__main__':
    unittest.main()