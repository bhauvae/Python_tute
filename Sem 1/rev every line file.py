text = open("text.txt",'r')
str = text.read()
l = str.split('\n')

for i in range(len(l)):
    print(l[i][::-1])
