def mean(list):
    return sum(list) / len(list)


def median(list):
    list.sort()

    if len(list) % 2 == 0:
        return (list[len(list) // 2] + list[len(list) // 2 + 1]) / 2
    else:
        return list[len(list) // 2]


def mode(list):
    frequency = {}
    high = 0
    for i in list:
        frequency[i] = list.count(i)

    for i in frequency:
        if frequency[i] > high:
            high = frequency[i]

    for i in frequency:
        if frequency[i] == high:
            return i


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

print(list, mean(list), median(list), mode(list))
if mode(list) == 3*median(list)-2*mean(list):
    print("true")
