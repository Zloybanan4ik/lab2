a = float(input("Input a: "))
s = input('Input "+", "-", "*", "/", "^", "sqrt", or "abs": ' )

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
else:
    print('Invalid type operation!!!')
