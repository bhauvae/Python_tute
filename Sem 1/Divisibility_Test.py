a = int(input("Specify the lower bound: "))
b = int(input("Specify the Upper Bound: "))
c = int(input("The number to test the divisibility with: "))
print("\nThe numbers following the criteria")
for i in range(a, b):
    if i % c == 0:
        print(i)
