
#################################
## Animal abstract data type 
#################################
#class Animal(object):
#    def __init__(self, age):
#        self.age = age
#        self.name = None
#    def get_age(self):
#        return self.age
#    def get_name(self):
#        return self.name
#    def set_age(self, newage):
#        self.age = newage
#    def set_name(self, newname=""):
#        self.name = newname
#    def __str__(self):
#        return "animal:"+str(self.name)+":"+str(self.age)


##################################
### Use of class variables  
##################################
class Animal(object):
    count = 1
    def __init__(self, age):
        self.age = age
        self.name = None
        self.id = str(Animal.count).zfill(9)
        Animal.count += 1
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname = 'George'):
        self.name = newname
    def __str__(self):
        typeName = self.__class__.__name__
        return typeName + ':' + str(self.name) + ':' + str(self.age) +\
               ':' + self.id
               
##Test Animal
#a = Animal(4)
#print(a)
#b = a
#print(b)
#a.set_name('Fluffy')
#print(a)
#print(b)
#c = Animal(5)
#c.set_name("Fluffy")
#print(c)
#print(a == c)

class Animal(object):
    count = 1
    def __init__(self, age):
        self.age = age
        self.name = None
        self.id = str(Animal.count).zfill(9)
        Animal.count += 1
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname = 'George'):
        self.name = newname
    def __str__(self):
        typeName = self.__class__.__name__
        return typeName + ':' + str(self.name) + ':' + str(self.age) +\
               ':' + self.id
    def __eq__(self, other):
        return self.name == other.name
#    def __eq__(self, other):
#        return self.id == other.id

#a = Animal(4)
#b = a
#a.set_name('Fluffy')
#c = Animal(5)
#c.set_name("Fluffy")
#print(a == c)

class KomodoDragon(Animal):
    count = 1
    def __init__(self, age, mother, father = None):
        Animal.__init__(self, age)
        self.mother = mother
        self.father = father
        self.id = str(KomodoDragon.count).zfill(9)
        KomodoDragon.count += 1
    def getParents(self):
        return (self.mother, self.father)

###Test Dragon        
#print('Test Dragon')
#a = KomodoDragon(4,'Betsy')
#print(a)
#a.set_name('Fluffy')
#print(a)
#a.set_name()
#print(a)
#b = KomodoDragon(5, 'Suzy')
#b.set_name('Fluffy')
#print(b)
#c = Animal(6)
#c.set_name('Guha')
#print(c)

class myStr(str):
    def __init__(self, val):
        str.__init__(val)
    def hasMIT(self):
        return 'M' in self and 'I' in self and 'T' in self
    def caseInsensitiveEq(self, other):
        return self.lower() == other.lower()
        
s = 'aTMI'
print(len(s))
#print(s.hasMIT())

s = myStr('aTMI')
print(s == 'atmi')
print(s.caseInsensitiveEq('atmi'))


class myStr(str):
    def __init__(self, val):
        str.__init__(val)
    def hasMIT(self):
        return 'M' in self and 'I' in self and 'T' in self
    def __eq__(self, other):
        return self.lower() == other.lower()
        
#ms1 = myStr('a')
#ms2 = myStr('A')
#s1 = 'A'
#s2 = 'a'
#print(s1 == s2)
#print(ms1 == ms2)
#

class passwordFile(object):
    def __init__(self):
        self.users = {}
    def addUser(self, name, password):
        if name in self.users:
            raise ValueError('duplicate user')
        self.users[name] = password
    def changePassword(self, name, oldPassword,
                       newPassword):
        if name not in self.users:
            raise ValueError('no such user')
        if self.users[name] == oldPassword:
            self.users[name] = newPassword
            print('Password changed.')
        else:
            raise ValueError('bad password')

#pwords = passwordFile()
#pwords.addUser('John', 'Guttag')
#old = 'guttag'
#pwords.changePassword('John', old, '6.00')

import time

def timeFunc(f, arg):
    print('Timing', f.__name__)
    for i in range(3):
        t0 = time.clock()
        f(arg)
        t1 = time.clock() - t0
        print('Wall time =', t1, 'sec.')

def cTof(c):
    return c*9/5 + 32

def count(x):
    total = 0
    for i in range(x):
        total += i
    return total

#timeFunc(cTof,  100000)
#timeFunc(count, 100000)

def power(x, e):
    """
    Assumes x a float, e a positive int
    Returns x**e
    """
    res = 1
    for i in range(e):
        res *= x
    return res
    
def isIn(L, e):
    for elem in L:
        if elem == e:
            return True
    return False

