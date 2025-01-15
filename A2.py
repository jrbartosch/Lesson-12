num1 = int(input('Please Enter a Number: '))
num2 = int(input('Please Enter a Number: '))
print ('Prime Numbers Between', num1, 'and', num2, 'Are:')
for num in range (num1, num2 + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i == 0):
                break
        else:
            print (num)