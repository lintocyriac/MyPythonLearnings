

def operation(a,b,c):
    print(f'{a} + {b} is {a+b}')
    print(f'{a} * {c} is {a*c}')
    print(f'{b} * {c} is {b*c}')

print("Enter the First String Value :")
a = (input())
print(f'Your First String Value is: {a} ')
print("Enter the Second String Value :")
b = (input())
print(f'Your First String Value is: {b} ')
print("Enter a Number :")
c = int(input())
print(f'You Entered number : {c} ')

operation(a,b,c)

