n = int(input("number "))
k = int(input("enter k "))
t = n
d = 0
while t > 0:
    t = t // 10
    d = d + 1

for i in range(k):
    a = n % (10 ** (d - 1))
    d1 = (n - a) // (10 ** (d - 1))
    n = (a * 10) + d1
print(n)
