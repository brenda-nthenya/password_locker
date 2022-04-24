import unittest
from user import User

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

    

if __name__ == '__main__':
    unittest.main()