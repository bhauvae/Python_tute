a = int(input("Enter marks of Subject A: "))
b = int(input("Enter marks of Subject B: "))
c = int(input("Enter marks of Subject C: "))
d = int(input("Enter marks of Subject D: "))
e = int(input("Enter marks of Subject E: "))
g = (a + b + c + d + e) / 5

if g in range(85, 101):
    print("The grade is A")
elif g in range(75, 85):
    print("The grade is B")
elif g in range(0, 75):
    print("The grade is C")
