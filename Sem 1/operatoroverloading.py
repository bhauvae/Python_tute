'''
Polymorphism: Operator Overloading
''' 
class Point:

    def __init__(self,x,y): #self is the implicit argument that refers to the current object
        self.x=x
        self.y=y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) +")"

    def __add__(self,other):
        newx = self.x + other.x
        newy = self.y + other.y
        
        newPoint = Point(newx,newy)
        return newPoint
    '''
    Overload the == and != operator for this class and
    demonstrate its use to compare two points
    '''

def main():
        
    p1=Point(2,3)
    print("P1 is ",p1)

    p2=Point(7,-3)
    print("P2 is ",p2)

    p3=p1+p2
    print("After adding p1 and p2",p3)

if __name__ == '__main__':
    main()
'''
Code Visualization via pythontutor.com
'''
