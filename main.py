import math

a = float(input("Input a: "))
s = input('Input "+", "-", "*", "/", "^", "sqrt", "abs", or "log": ' )

if s == '-':
    b = float(input("Input b: "))
    print(a-b)
elif s == '+':
    b = float(input("Input b: "))
    print(a+b)
elif s == '*':
    b = float(input("Input b: "))
    print(a*b)
elif s == '/':
    b = float(input("Input b: "))
    if b != 0:
        print(a/b)
    else:
        print("Division by zero is not allowed!")
elif s == '^':
    b = float(input("Input b: "))
    print(a**b)
elif s == 'sqrt':
    print(math.sqrt(a))
elif s == 'abs':
    print(abs(a))
elif s == 'log':
    if a > 0:
        print(math.log(a))
    else:
        print("Logarithm of non-positive number is not defined!")
else:
    print('Invalid type operation!!!')
