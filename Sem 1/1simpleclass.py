#defining a class Person with no body
class Person:
    pass

#creating objects of the class Person
p1=Person()
p2=Person()


class Person2:
    name=""
    DOB=""
    address=""

    def show(self):
        print(self.name)
        print(self.DOB)
        print(self.address)

#creating a new instance/object
p2 = Person2()

#modifying the data members
p2.name="Amit"
p2.DOB = "11-10-1992"
p2.address="12,Sec-4,Rohini"

#calling an object's method
p2.show()

p3=Person2()

p3.name="Rohit"
p3.DOB = "21-08-1995"
p3.address="32,Sec-4,Dwarka"

p3.show()

'''
Code Visualization via pythontutor.com
https://pythontutor.com/visualize.html#code=class%20Person%3A%0A%20%20%20%20pass%0A%0Ap1%3DPerson%28%29%0A%0A%0Aclass%20Person2%3A%0A%20%20%20%20name%3D%22%22%0A%20%20%20%20DOB%3D%22%22%0A%20%20%20%20address%3D%22%22%0A%0A%20%20%20%20def%20show%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28self.name%29%0A%20%20%20%20%20%20%20%20print%28self.DOB%29%0A%20%20%20%20%20%20%20%20print%28self.address%29%0A%0A%23creating%20a%20new%20instance/object%0Ap2%20%3D%20Person2%28%29%0A%0A%23modifying%20the%20data%20members%0Ap2.name%3D%22Amit%22%0Ap2.DOB%20%3D%20%2211-10-1992%22%0Ap2.address%3D%2212,Sec-4,Rohini%22%0A%0A%23calling%20an%20object's%20method%0Ap2.show%28%29%0A%0Ap3%3DPerson2%28%29%0A%0Ap3.name%3D%22Rohit%22%0Ap3.DOB%20%3D%20%2221-08-1995%22%0Ap3.address%3D%2232,Sec-4,Dwarka%22%0A%0Ap3.show%28%29%0A&cumulative=false&curInstr=23&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''
