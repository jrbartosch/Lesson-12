num1 = int(input('Please Enter the Starting Number of the Range: '))
num2 = int(input('Please Enter the Ending Number of the Range: '))

print('Prime Numbers Between', num1, 'and', num2, 'are:')

for num in range(num1, num2 + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)