# write a function nearly _equal to test whether two strings are nearly equal. two strings a and b are nearly equal when
# a can be generated by a single mutation on b.

def nearly_equal(str1, str2):
    count = 0
    i = j = 0
    while i < len(str1) and j < len(str2):
        if (str1[i] != str2[j]):
            count = count + 1
            if (len(str1) > len(str2)):
                i = i + 1
            elif (len(str1) == len(str2)):
                pass
            else:
                i = i - 1
        if count > 1:
            return False
        print(i,j)
        i = i + 1
        j = j + 1
    if count < 2:
        return True


str1 = input("enter first string:: ")
str2 = input("enter second string:: ")
boolean = nearly_equal(str1, str2)

if boolean:
    print("strings are nearly equal.")
else:
    print("strings are not equal.")