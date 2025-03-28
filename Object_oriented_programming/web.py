class Users():
    '''models a class called user'''
    def __init__(self,first_name,last_name,user_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.age=age

    def describe_user(self):
        print(
            'first name :'+self.first_name.title()+'\n',
            'last name :'+self.last_name.title()+'\n',
            'user name :'+self.user_name.title()+'\n',
            'age :'+str(self.age),
        )

    def greet_user(self):
        print('hello !, how are you doing '+self.first_name.title()+' '+self.last_name.title())

class priviledges():
    def __init__(self):
        self.priviledges=['can add post','can delete post','can ban user']

    def show_priviledges(self):
        '''prints out a list of all actions admin can carry_out'''
        print('here are all actions that can be carried out by admin:')
        for priviledge in self.priviledges:
            print('-'+priviledge.title())

class Admin(Users):
    def __init__(self,first_name,last_name,user_name,age=''):
        super().__init__(first_name,last_name,user_name,age)
        self.priviledges=['can add post','can delete post','can ban user']
        self.rights=priviledges()
        
    def show_priviledges(self):
        '''prints out a list of all actions admin can carry_out'''
        print('here are all actions that can be carried out by admin:')
        for priviledge in self.priviledges:
            print('-'+priviledge.title())
