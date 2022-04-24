from dis import show_code
from user import User
from credentials import Credentials

def create_user(user_name, password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name, password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    User.save_user()

def display_user():
    '''Function to display all users'''
    return User.display_user()

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
    check_user = Credentials.verify_user(username,password)
    return check_user


def create_credential(account,userName,password):
    """ Function that creates new credentials for a given user account """
    new_credential = Credentials(account,userName,password)
    return new_credential

def save_credential(credentials):
    """
    Function to save Credentials to the credentials list
    """
    Credentials. save_credential()


def display_accounts():
    """ Function that returns all the saved credential. """
    return Credentials.credential_display()

def delete_credential(credentials):
    """ Function to delete a Credentials from credentials list """
    Credentials.delete_credential()


def find_credential(account):
    """ Function that finds a Credentials by an account name and returns the Credentials that belong to that account """
    return Credentials.find_credential(account)

def account_exist(account):
    """ Function that check if a Credentials exists with that account name and return true or false """
    return Credentials.account_exist(account)

def copy_password(account):
    """
    A func that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_pass = Credentials.pass_generator()
    return auto_pass

def main():
    print ("Hello Welcome to your Accounts Password Locker...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code = input("").lower().strip()
    if short_code == ""
    