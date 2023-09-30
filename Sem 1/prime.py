p = int(input('Enter the limit for sum: '))
print('\nThe primes below', p, ' are:')
s = 0
for num in range(2, p):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        s = s + num

print('\nThe sum of all the prime numbers is: ', s)
