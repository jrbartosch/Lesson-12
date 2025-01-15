num1 = int(input('Please Enter a Number: '))
num2 = num1
numlen = 0

while num2 > 0:
    numlen += 1
    num2 = int(num2 / 10)

if numlen >= 4:
    numlen = int(numlen / 2)
    check = 0
    mid1 = 0
    mid2 = 0
    while num1 > 0:
        remainder = num1 % 10
        if check == numlen:
            mid1 = remainder
        elif check == (numlen - 1):
            mid2 = remainder
        num1 = int(num1 / 10)
        check += 1

    if mid2 == 0:
        product = mid1 * mid1
    else:
        product = mid1 * mid2
    
    print('The Product of the Middle Digit(s) of that Number is', product)
else:
    print('Please Enter at Least Four Digits.')