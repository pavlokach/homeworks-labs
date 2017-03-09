from classroom import *
from building import *
from academicbuilding import *
classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)


def authorisation():
    logins = ['Admin', '']
    print('Please enter your login')
    login = input()

class User:
    usertypes = ['admin']
    ratings = {'admin': 100}

    def __init__(self, name):
        self.name = name
        self.entry_check(name)

    def entry_check(self, name = ''):
        if name.lower() == 'admin':
            self.admin_entry()
        else:
            self.user_entry()

    def user_entry(self):
        print('To check building info enter "check info"')
        if input() == 'check info':
            print(building)
        if input('If you would like to log out enter "log out"') == 'log out':
            self.entry_check()


    def admin_entry(self):
        print('To create new usertype input "add usertype", enter to leave')
        if input() == 'add usertype':
            self.create_usertype()
        if input('If you would like to log out enter "log out"') == 'log out':
            self.entry_check()

    def create_usertype(self):
        newname = input('Please enter the name of the new usertype: ')
        if newname not in self.usertypes:
            self.usertypes.append(newname)
            #self.ratings[newname] = input('Please enter level of access that user has(ex: 50): ')


#user = User(input('Enter your username: '))
