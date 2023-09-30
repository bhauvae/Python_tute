def dups(list):
    d = {}
    for i in list:
        d[i] = list.count(i)

    for i in d:
        if d[i] > 1:
            print(i)


dups([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8, 2, 9, 0, 7, 7, 7, 3, 8, 5, 5, 5, 7])
