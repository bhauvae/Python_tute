'''
This code demonstrates the Multiple Inheritance among Classes in Python
'''
class X:
    def __init__(self,x):
        self.x=x

    def showX(self):
        print("x:",self.x)


class Y:
    def __init__(self,y):
        self.y=y

    def showY(self):
        print("y:",self.y)


class Z(X,Y):
    def __init__(self,x,y,z):
        X.__init__(self,x)
        Y.__init__(self,y)
        self.z=z

    def showZ(self):
        print("z:",self.z)

    def showAll(self):
        print("x:",self.x) #super class variables are accessible here
        print("y:",self.y) #super class variables are accessible here
        print("z:",self.z)

objz = Z(1,2,3)
objz.showX()
objz.showY()
objz.showZ()

objz.showAll()

#Code Vizualization on pythontutor.com
#https://pythontutor.com/visualize.html#code='''%0AThis%20code%20demonstrates%20the%20Multiple%20Inheritance%20among%20Classes%20in%20Python%0A'''%0Aclass%20X%3A%0A%20%20%20%20def%20__init__%28self,x%29%3A%0A%20%20%20%20%20%20%20%20self.x%3Dx%0A%0A%20%20%20%20def%20showX%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22x%3A%22,self.x%29%0A%0A%0Aclass%20Y%3A%0A%20%20%20%20def%20__init__%28self,y%29%3A%0A%20%20%20%20%20%20%20%20self.y%3Dy%0A%0A%20%20%20%20def%20showY%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22y%3A%22,self.y%29%0A%0A%0Aclass%20Z%28X,Y%29%3A%0A%20%20%20%20def%20__init__%28self,x,y,z%29%3A%0A%20%20%20%20%20%20%20%20X.__init__%28self,x%29%0A%20%20%20%20%20%20%20%20Y.__init__%28self,y%29%0A%20%20%20%20%20%20%20%20self.z%3Dz%0A%0A%0A%20%20%20%20def%20showZ%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22z%3A%22,self.z%29%0A%0A%20%20%20%20def%20showAll%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22x%3A%22,self.x%29%20%23super%20class%20variables%20are%20accessible%20here%0A%20%20%20%20%20%20%20%20print%28%22y%3A%22,self.y%29%20%23super%20class%20variables%20are%20accessible%20here%0A%20%20%20%20%20%20%20%20print%28%22z%3A%22,self.z%29%0A%0Aobjz%20%3D%20Z%281,2,3%29%0Aobjz.showX%28%29%0Aobjz.showY%28%29%0Aobjz.showZ%28%29%0A%0Aobjz.showAll%28%29&cumulative=false&curInstr=34&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
