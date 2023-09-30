class Complex_Number:
    def __init__(self, real, imaginary):
        self.real = real
        self.__imaginary = imaginary

    def __str__(self):
        return "{} + {} i ".format(self.real, self.__imaginary)

    def get_imaginary(self):
        return self.__imaginary

    def set_imaginary(self, i_part):
        self.__imaginary = i_part
    def __add__(self,other):
        new_real = self.real + other.real
        new_imaginary =self.__imaginary + other.__imaginary
        return Complex_Number(new_real,new_imaginary)
    def __

z5 =Complex_Number()
z5.set_imaginary()
z1=Complex_Number(2,3)
z2=Complex_Number(1,2)
print(z1)
z3= z1 + z2
print (z3)