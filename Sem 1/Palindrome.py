a = int(input("Enter a number: "))
o = a
r = 0
while o != 0:
    r = r * 10 + o % 10
    o = o // 10
if a == r:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")
