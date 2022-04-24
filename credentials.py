
class Credential:

    credential_list = []

    def __init__(self,account, username, password):
        self.account = account
        self.username = username
        self.password = password

    def save_credential(self):
        ''' Saves credential object to the credential list'''
        Credential.credential_list.append(self)
