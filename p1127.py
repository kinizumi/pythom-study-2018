##def try_catch_dict(dict):
##    try:
##       print(dict['t'], dict.t)
##       
##    except (AttributeError, NameError, KeyError) as e:
##            print(e)
##    for key, value in dict.items():
##        try:
##            print(key, value[3])
##            raise NameError
##        except Exception as e:
##            print('no!! %s'%e)
##
##
##dict = {'montreal':25,'toronto':[1,2,3]}
##try_catch_dict(dict)
class MyExpt(Exception):
    def __init__(self, msg, json):
        super.__init__(self, message)
        self.json = json


def printExpt():
    try:
        print('aaaaa')
        raise MyExpt('bbbbb')
        print('ccccc')
    except MyExpt as e:
        print(e)

printExpt()
