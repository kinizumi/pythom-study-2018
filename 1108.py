##import sys
##sys.path.append('E:\\pythonSep2018')
##import p1108
##sys.path.remove('E:\\pythonSep2018')
##sys.path.remove('E:\\pythonSep2018')
##print(sys.path)
##import p1108
##print(p1108)
import datetime
now = datetime.datetime.now()
class User:
    name = 'tom'
    age = 0
    message = 'you alrady older than 100'
    def countAge(self, name, age):
        if age > 100:
            print(self.message)
        print(' Hello {}, you will be 100 in the year {} '.format(name, now.year + (100 - age)))

u = User()
##u.countAge('mike', 50)

name = input('what is your name')
print(9*"hallo {} \n".format(name))
