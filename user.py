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

    

    