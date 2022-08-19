#Function to find Mid letter 
def findmidchar(a,b):
    print(f"Mid index of string '{a}' is {b//2} ")    
    if (b%2 != 0 ):
        print(f"Middle character in '{a}' is {a[b//2]}")
    else:
        print(f"Middle character in '{a}' is '{a[b//2 - 1]}' and '{a[b//2]}'")

#Function to find first and last letter and length
def operation(a):
    b = int(len(a))
    print(f"First character in '{a}' is '{a[0]}'")
    print(f"Last character in '{a}' is '{a[-1]}'")
    print(f"Length of string '{a}' is '{b}'")
    findmidchar(a,b)

#Accept input
print("Enter a String Value :")
a = (input())
print(f'You entered : {a} ')

operation(a)
