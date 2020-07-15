x = int(input('Please enter a number from 1 to 10 (greater than 10 or less than 1 will cause calculation error)'))
print("In the process of computing, the program will display the calculated data in real time.")
sum = x * 2
print('%s*2=%s' % (x, sum))
num = sum
sum += 5
print('%s+5=%s' % (num, sum))
num = sum
sum = sum * 50
print('%s*50=%s' % (num, sum))
y = input('Did you celebrate your birthday? (entered or failed)')
if y == 'entered':
    num = sum
    sum += 1770
    print('%s+1770=%s' % (num, sum))
elif y == 'failed':
    num = sum
    sum += 1769
    print('%s+1769=%s' % (num, sum))
a = int(input('Your year of birth is: (four digits)'))
num = sum
sum = sum - a
print('%s-%s=%s' % (num, a, sum))
num = x
x = x * 100
print('%s*100=%s' % (num, x))
num = sum
sum = sum - x
print('%s-%s=%s' % (num, x, sum))
print('Your age is: %s years old' % sum)
