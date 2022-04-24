import unittest
import pyperclip

from user import User
from credentials import Credentials


class TestUser(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('Brenda','pebbles')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.user_name,'Brenda')
        self.assertEqual(self.new_user.password,'pebbles')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
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

    def test_credential_display(self):
        '''Returns a list of all credentials'''
        self.assertEqual(Credentials.credential_display(), Credentials.credentials_list)

    # def test_copy_username(self):
    #     '''Test to confirm that the account can be copied'''
    #     self.new_credential.save_credential()
    #     Credentials.copy_username("Brenda")

    #     self.assertEqual(self.new_credential.account, pyperclip.paste())



if __name__ == '__main__':
    unittest.main()