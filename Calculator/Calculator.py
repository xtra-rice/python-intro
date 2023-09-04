# x,y,z = 'Julia', 'Franchesca', 'Borromeo'

# print(x + y + z)

# ulam = ['menudo', 'kaldereta', 'sinigang']
# a,b,c = ulam

# print(a,b,c)


def add(x, y,):
    return x + y


def subtract(x, y,):
    return x - y


def multiply(x, y,):
    return x * y


def divide(x, y,):

    if y == 0:
        return 'Cannot divide by zero'
    return x / y


while True:

    print('Select operation:')
    print('1. Add')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Divsion ')
    operation = input("Enter choice 1/2/3/4 or Type 'q' to exit. ")

    if operation == "q":
        break
    elif operation in ('1', '2', '3', '4'):
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))

    if operation == "1":
        print(add(n1, n2))
        print('\n')
    elif operation == '2':
        print(subtract(n1, n2))
        print('\n')
    elif operation == '3':
        print(multiply(n1, n2))
        print('\n')
    elif operation == '4':
        print(divide(n1, n2))
        print('\n')
    else:
        print('Invalid support')
        print('\n')
