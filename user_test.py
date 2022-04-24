import unittest
from user import User
from credentials import Credentials

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
         
    def test_save_credential(self):

        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''Removes all other instances created during the test.'''
        Credentials.credentials_list = []

    def test_save_multiple_credential(self):
        '''Tests the ability to store multiple credentialsin the credential list'''
        self.new_credential.save_credential()
        test_credential = Credentials("Twitter", "Bots", "pancakes")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        ''' Tetst the delete contact to test if we can remove a credential'''
        self.new_credential.save_credential()
        test_credential = Credentials("Twitter", "Bots", "pancakes")
        test_credential.save_credential()

        test_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)

if __name__ == '__main__':
    unittest.main()