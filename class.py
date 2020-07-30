#simple class
class aa:
    x = 10
    #print(x)
obj = aa()  #object of class
print(obj.x)

# class with constructor
class name():
    # creating constructor
    def __init__(self,name):
        self.n = name
        self.i = "india"  #self parameter
    # self is current instant in class
    def user(self):  
        print('''\nhello user {}\naddress is {}'''.format(self.n,self.i))
us = input("enter your name")
objs = name(us)
objs.user()

'''
 we can delete object and after this that object does not exixts
del(obj)
print(obj)
'''


