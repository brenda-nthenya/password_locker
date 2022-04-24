
class Credentials:

    credentials_list = []

    def __init__(self,account, username, password):
        self.account = account
        self.username = username
        self.password = password

    def save_credential(self):
        ''' Saves credential object to the credential list'''
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        '''Deletes a credential object'''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls,account):
        '''Method takes an account name and returns credentials that match'''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def account_exist(cls, account):
        '''
        Method checks if an account exists
        Returns true or false.
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def credential_display(cls):
        '''Dsiplays the contents of the credentials list'''
        return cls.credentials_list