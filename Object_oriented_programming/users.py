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
