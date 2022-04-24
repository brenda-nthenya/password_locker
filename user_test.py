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

    def test_find_credential(self):
        self.new_credential.save_credential()
        test_credential = Credentials("Twitter", "Bots", "pancakes")
        test_credential.save_credential()

        ''' 
        Takes an account name and returns the credentials that match
        the credentials
        '''
        my_credential = Credentials.find_credential("Twitter")
        self.assertEqual(my_credential.account,test_credential.account)

    def test_account_exist(self):
        '''Tests if the account one is searching for exists'''
        self.new_credential.save_credential()
        test_credential = Credentials("Twitter", "Bots", "pancakes")
        test_credential.save_credential()

        account_exist = Credentials.account_exist("Twitter")
        self.assertTrue(account_exist)


if __name__ == '__main__':
    unittest.main()