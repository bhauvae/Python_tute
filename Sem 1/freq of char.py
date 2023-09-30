str = "hello my name is, my name is whattt"

dict ={}

#for i in str:
#    dict[i] = str.count(i)
for i in str:
    if i in dict:
        dict[i] = dict[i]+1
    else:
        dict[i] = 1
print(dict)