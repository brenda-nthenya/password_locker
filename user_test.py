import unittest
from user import User
from credentials import Credential

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


class TestCredential(unittest.TestCase):


    '''Tests the functionalities of the Credentials class'''

    def setUp(self):
        '''Sets up the method to run before each test'''
        self.new_credential = Credential("Facebook", "Brenda", "asdfg123")
    
    def test_init(self):
        ''' Test if the object has correctly been initialised'''

        self.assertEqual(self.new_credential.account, 'Facebook')
        self.assertEqual(self.new_credential.username, "Brenda")
        self.assertEqual(self.new_credential.password, "asdfg123")
         
    def test_save_credential(self):

        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def tearDown(self):
        '''Removes all other instances created during the test.'''
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        '''Tests the ability to store multiple credentialsin the credential list'''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "Bots", "pancakes")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

if __name__ == '__main__':
    unittest.main()