import auth


class GameAuth:
    def __init__(self, authorizor):
        self.authorizor = authorizor
        self.__admin = 'admin'
        self.__admin_pass = 'password'
        self.authorizor.authenticator.add_user(self.__admin, self.__admin_pass)
        self.authorizor.add_permission('admin')
        self.authorizor.permit_user('admin', self.__admin)

    def login(self):
        # Log in
        return self.authorizor.authenticator.login(input('Login: '),
                                                   input('Password: '))

    def add_user(self):
        # Add user
        username = self.authorizor.authenticator.logged_user
        if self.authorizor.check_permission('admin', username):
            self.authorizor.authenticator.add_user(input('New user login: '),
                                                   input('New user password: '))

    def permit_user(self):
        # Permit user
        username = self.authorizor.authenticator.logged_user
        if self.authorizor.check_permission('admin', username):
            self.authorizor.permit_user(input('Type of permission: '),
                                        input('Username: '))

    def play(self):
        # Insert battleship here
        print('We gonna make this game great again!')

    def auth_system(self):
        # All methods for authorization called here
        type_operation = {'add user', 'permit user', 'play', 'login'}
        print('To exit press Enter.')
        while True:
            operation = input('Choose an operation: login, play, permit user, add user\n')
            if operation in type_operation:
                try:
                    eval('self.{}()'.format('_'.join(operation.split())))
                except auth.NotLoggedInError:
                    print('Not logged in. Please log in. Or do not')
                except auth.UsernameAlreadyExists:
                    print('Username already exists. Unlike your love life.')
                except auth.PasswordTooShort:
                    print('What is too short? Your password.')
                except (auth.InvalidUsername, auth.InvalidPassword):
                    print('Who is an invalid? Your username or password.')
                except auth.NotPermittedError:
                    print('You shall not pass! (Not permitted)')
                except auth.PermissionError:
                    print('I already built a wall. You are not permitted.')
            elif not operation:
                break
            else:
                print('Not correct name of operation. Try again.')
            print('To exit press Enter.')

'''
authenticator = auth.Authenticator()
authorizor = auth.Authorizor(authenticator)
game = GameAuth(authorizor)
game.auth_system()
'''
#def hhh():
from classroom import Classroom
classroom_name = 'ggg'
classroom_number = '1'
classroom_capacity = 80
classroom_equipment = ['PC']
#Classroom(classroom_number, classroom_capacity, classroom_equipment)
exec ('{0} = Classroom(\'{1}\', {2}, {3})'.format(classroom_name, classroom_number, classroom_capacity, classroom_equipment))
classrooms = []

print(type(ggg))
x= 'y_017'
#print(eval(y))