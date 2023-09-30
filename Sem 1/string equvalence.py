word1 = "aaaa"
word2 = "bccb"
fd = {}
flag = 0
for i in word1+word2:
    fd[i]=abs(word1.count(i)-word2.count(i))

for i in fd:
    if fd[i]>3:
        flag = 1
if flag == 1:
    print("false")
else:
    print("true")