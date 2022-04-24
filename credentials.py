
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
