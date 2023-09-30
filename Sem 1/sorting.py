starting_list = [2, 3, 7, 9, 4, 5, 1, 6, 8,3,3 ]
sorted_list = []

print(starting_list)
for i in range(len(starting_list)):
    roll_number = 0
    for j in starting_list:
        if j > roll_number:
            roll_number = j
    print(roll_number)
    sorted_list.append(roll_number)
    starting_list.remove(roll_number)

print(sorted_list)
