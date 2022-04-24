class User:

    user_list = []

    '''
    Class that creates nre users of password locker
    '''
    def __init__(self,user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        ''' Deletes an account from the list'''
        User.user_list.remove(self)

    

    