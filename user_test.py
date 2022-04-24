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

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


class TestCredentials(unittest.TestCase):

    '''Tests the functionalities of the Credentials class'''

    def setUp(self):
        '''Sets up the method to run before each test'''
        self.new_credential = Credentials("Facebook", "Brenda", "asdfg123")
    
    def test_init(self):
        ''' Test if the object has correctly been initialised'''

        self.assertEqual(self.new_credential.account, 'Facebook')
        self.assertEqual(self.new_credential.username, "Brenda")
        self.assertEqual(self.new_credential.password, "asdfg123")
         
    

if __name__ == '__main__':
    unittest.main()