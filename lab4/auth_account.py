import auth
import building
from classroom import Classroom


class BuildingChecker:
    def __init__(self, authorizor):
        # Initializing variables
        self.authorizor = authorizor
        self.__admin = 'admin'
        self.__admin_pass = 'adminadmin'
        self.authorizor.authenticator.add_user(self.__admin, self.__admin_pass)
        self.authorizor.add_permission('admin')
        self.authorizor.permit_user('admin', self.__admin)

    def login(self):
        # For logging into any created user
        return self.authorizor.authenticator.login(input('Login: '),
                                                   input('Password: '))

    def check_building(self):
        # Finding out adress and classrooms info
        username = self.authorizor.authenticator.logged_user
        if self.authorizor.check_permission('admin', username):
            for room in building.classrooms:
                print(room)

    def add_classroom(self):
        # For creating new Classroom variable
        username = self.authorizor.authenticator.logged_user
        if self.authorizor.check_permission('admin', username):
            classroom_name = input('Enter classroom name: ')
            while classroom_name in building.classrooms:
                classroom_name = input('Enter new classroom name: ')
            classroom_number = str(input('Enter classroom number: '))
            classroom_capacity = input('Enter classroom capacity: ')
            classroom_equipment = input('Enter classroom equipment(ex: TV projector): ').split(' ')
            building.classrooms.append(Classroom(classroom_number, classroom_capacity, classroom_equipment))

    def add_user(self):
        # For creating new user
        username = self.authorizor.authenticator.logged_user
        if self.authorizor.check_permission('admin', username):
            self.authorizor.authenticator.add_user(input('Enter login for new user: '),
                                                   input('Enter password for new user: '))

    def add_permition(self):
        # For adding admin authority to any user
        username = self.authorizor.authenticator.logged_user
        if self.authorizor.check_permission('admin', username):
            self.authorizor.permit_user(input('Enter permision name: '),
                                        input('Permit which user: '))

    def auth_system(self):
        # All methods for authorization called here
        type_operation = {'add user', 'add permition', 'login', 'check building', 'add classroom'}
        while True:
            print('To exit enter Exit.')
            operation = input('Choose an operation: login, check building, add classroom, add user, add permition\n')
            if operation in type_operation:
                try:
                    eval('self.{}()'.format('_'.join(operation.split())))
                except auth.NotLoggedInError:
                    print('Sorry:( You\'re not logged in')
                except auth.UsernameAlreadyExists:
                    print('This username already exists.')
                except auth.PasswordTooShort:
                    print('Short password => short....... memory?')
                except (auth.InvalidUsername):
                    print('Wrong username bro')
                except (auth.InvalidPassword):
                    print('Is it just me or your password is wrong?')
                except auth.NotPermittedError:
                    print('You have no power here!')
                except auth.PermissionError:
                    print('What if I told you there is no such permission')
            elif operation.lower() == 'exit':
                break
            else:
                print('Wrong operation. Enter again.')


authenticator = auth.Authenticator()
authorizor = auth.Authorizor(authenticator)
checker = BuildingChecker(authorizor)
checker.auth_system()
