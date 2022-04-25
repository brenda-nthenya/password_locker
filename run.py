#!/usr/bin/env python3

from ast import Continue
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
    user.save_user()

def display_user():
    '''Function to display all users'''
    return User.display_user()

def login_user(user_name,password):
    """
    function that checks whether a user exist and then login the user in.
    """
    check_user = Credentials.verify_user(user_name,password)
    return check_user


def create_credential(account,username,password):
    """ Function that creates new credentials for a given user account """
    new_credential = Credentials(account,username,password)
    return new_credential

def save_credential(credentials):
    """
    Function to save Credentials to the credentials list
    """
    Credentials. save_credential(credentials)


def display_accounts():
    """ Function that returns all the saved credential. """
    return Credentials.credential_display()

def delete_credential(credentials):
    """ Function to delete a Credentials from credentials list """
    Credentials.delete_credential(credentials)


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
    print('*'*30)
    print ("Hello Welcome to your Accounts Password Locker...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code = input("").lower().strip()
    print('*'*30)
    if short_code == "ca":
        print('KIndly input your user name')

        user_name = input('User_name: ')
        while True:
            print('*'*30)
            print("Please select either of the following:..\n GP - To auto generate a password \n TP - To type our own password ")
            password_option = input().lower().strip()
            if password_option == 'gp':
                password = generate_Password()
                print('*'*30)
                print(password)
                print('*'*30)
                break
               
            elif password_option == 'tp':
                print('*'*30)
                password = input("Enter Password\n")
                print('*'*30)
                break

            else:
                print('*'*30)
                print ('Invalid password. PLease try again')
                print('*'*30)
            
            save_user(create_user(user_name, password))

        print(f'Hello {user_name}. Your account has been created successfully')
    elif short_code == 'li':
        print ('Enter your username and password to log in:')
        user_name = input ('User name: ')
        password = input('Password: ')

        login = login_user(user_name, password)

        if login_user == login:
            print('*'*30)
            print(f'Hello {user_name}. Welcome to your password manager')
            print('\n')
            print('*'*30)

    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print ('Create new credentials')
            print ('*'*30)
            print ('Account Name: ')
            account = input()
            print ('*'*30)
            print ('Your account user name is: ')
            username = input()
            print ('*'*30)

            while True:
                print("Please select either of the following:..\n GenPass - To auto generate a password \n TPass - To type our own password ")
                password_option = input().lower()
                if password_option == 'genpass':
                    password = generate_Password
                    break
                elif password_option == 'tpass':
                    password = input("Enter Password: ")
                    break
                else:
                    print ('Invalid password. PLease try again')

            save_credential(create_credential(account, username, password))
            print('\n')
            print (f'Account: {account}, Username: {username}, Password: {password} created successfully')
        elif short_code == 'dc':
                if display_accounts():
                    print('*'*30)
                    print('Your saved accounts are: \n')
                    print('*'*30)
                    for account in display_accounts:
                        print(f"Account:{account.account} \n Username: {username} \n Password: {password}")
                    print ('*'*30)

                else:
                    print('*'*30)
                    print ('You have not saved any credential yet')
                    print('*'*30)
        elif short_code == 'fc':
            print("Enter the account name you are searching for:")
            search_account = input()
            if find_credential(search_account):
                search_credential = find_credential(search_account)
                print('*'*30)
                print (f'Account name: {search_credential}')
                print('*'*30)
                print(f'User name: {search_credential.username}\n Password: {search_credential.password}')
                print('*'*30)

            else:
                print('That account does not exist')

        elif short_code == "dc":
            if display_accounts():
                print('*'*30)
                print("Here's your list of acoounts: ")
                
                print('*' * 30)
                for account in display_accounts():
                    print(f" Account:{account} \n User Name:{username}\n Password:{password}")
                print('*' * 30)
            else:
                print('*'*30)
                print("You don't have any credentials saved yet..........")
                print('*'*30)

        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("*"*50)
                search_credential.delete_credential()
                print('*'*30)
                print('\n')
                print('*'*30)
                print(f"Your credentials for : {search_credential.account} successfully deleted!!!")
                print('*'*30)
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_Password()
            print('*'*30)
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
            print('*'*30)
        elif short_code == 'ex':
            print('*'*30)
            print("Thanks for using passwords store manager.. See you next time!")
            print('*'*30)
            break
        else:
            print('*'*30)
            print("Wrong entry... Check your entry again and let it match those in the menu")
            print('*'*30)
    
    else:
        print('*'*30)
        print("Please enter a valid input to continue")
        print('*'*30)

if __name__ == '__main__':
    main()
