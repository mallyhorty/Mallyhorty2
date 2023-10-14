def add(num1, num2, num3):
    return num1 + num2 - num3

def sub(num1, num2, num3):
    return num1 - num2 + num3

def multiply(num1, num2, num3):
    return num1 * num2 - num3

def divide(num1, num2, num3):
    return num1 / num2 * num3

num1 = float(input('input a number:'))
num2 = float(input('input a number:'))
num3 = float(input('input a number:'))

print('select the operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

choice = int(input('Enter operation choice btw (1-10):'))
if choice == 1:
    result = add(num1, num2, num3)
    print('Result:', result)
elif choice == 2:
    result = sub(num1, num2, num3)
    print('Result:', result)
elif choice == 3:
    result = multiply(num1, num2, num3)
    print('Result:', result)
elif choice == 4:
    result = divide(num1, num2, num3)
    print('Result:', result)
else:
    print('invalid choice')



