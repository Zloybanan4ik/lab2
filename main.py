a = float(input("Input a: "))
b = float(input("Input b: "))
s = input('Input "+", "-", "*", "/", or "^": ' )

if s == '-':
    print(a-b)
elif s == '+':
    print(a+b)
elif s == '*':
    print(a*b)
elif s == '/':
    if b != 0:
        print(a/b)
    else:
        print("Division by zero is not allowed!")
elif s == '^':
    print(a**b)
else:
    print('Invalid type operation!!!')
