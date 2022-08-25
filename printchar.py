#Function to find the slice of strings
def print_operation(a):
    b = int(len(a))
    count =0
    while count < b:
        print(a[count])
        count=count +1
        
def print_operationRev(a):
    b = int(len(a))
    count = -1
    while count >-b-1:
        print(a[count])
        count=count -1

#Accept input
print("Enter a String Value :")
a = (input())
print(f'You entered : {a} ')
print(f'Print character of <{a}>  \n')
print_operation(a)
print(f'Print character of <{a}> in reverse \n')
print_operationRev(a)