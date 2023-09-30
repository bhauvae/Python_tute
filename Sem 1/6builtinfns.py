'''
Built-in functions for classes
''' 
class Person:
    objCount=0

    def __init__(self,name,DOB,address): #self is the implicit argument that refers to the current object
        self.name=name
        self.DOB=DOB
        self.address=address

        #increase the value of count as soon as new object is created
        Person.objCount += 1

    def show(self):
        print(self.name)
        print(self.DOB)
        print(self.address)

    def __str__(self):
        return "Name: " + self.name + "\n" +\
                "DOB: " + self.DOB + "\n" +\
                "Address: " + self.address

    def __del__(self):
        print("Object Deleted")
        Person.objCount -=1
    
        

p1 =Person('Amit','11-10-1992','12,Sec-4,Rohini')
print(p1)
print("No. of active objects:",Person.objCount)

p2 = Person("Rohit","21-08-1995","32,Sec-4,Dwarka")
print(p2)
print("No. of active objects:",Person.objCount)

del p1
print("No. of active objects:",Person.objCount)

del p2
print("No. of active objects:",Person.objCount)

'''
Code Visualization via pythontutor.com
'''
