'''
polymorphism means one thing and many forms
Polymorphism: Function Overloading - different function is executed based
                                     on the number of arguments passed to it
'''
'''
def area(side1):
    return side1 ** 2

print("Area of square" ,area(5))


def area(side1,side2):
    return side1 * side2

print("Area of Rectangle" ,area(5,2.5))    
print("Area of square" ,area(4))
'''

def area(side1,side2=None):
    if side2 == None:
        return side1 ** 2
    else:
        return side1 * side2

print("Area of Rectangle" ,area(5,2.5))    
print("Area of square" ,area(4))

