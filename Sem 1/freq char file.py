txt = open('text.txt', 'r')

dict = {}
str = txt.read()
print(str)
for i in str:
    if i != " " and i != "\n":
        dict[i] = str.count(i)

print(dict)
