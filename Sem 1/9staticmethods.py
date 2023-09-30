'''
STATIC METHODS: Methods that are not associated with any instance of the class.
These are class-level methods.
'''
class Person:
    objCount=0

    def __init__(self,name,DOB,address):
        self.name=name
        self.DOB=DOB
        self.address=address

        #increase the value of count as soon as new object is created
        Person.incObjCount()

    def show(self):
        print(self.name)
        print(self.DOB)
        print(self.address)

    @staticmethod
    def incObjCount():
        Person.objCount +=1

    @staticmethod
    def getObjCount():
        return Person.objCount

p1 =Person('Amit','11-10-1992','12,Sec-4,Rohini')
print("No. of active objects:",Person.getObjCount())

'''
'''
