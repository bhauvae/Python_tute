l1 = [1, 2, 3, 4, 5, 6]
l2 = ['a', 'b', 'c', 'd', 'e']
d = {}
for key in l1:
    for value in l2:
        d[key] = value
        l2.remove(value)
        break

print(d)
