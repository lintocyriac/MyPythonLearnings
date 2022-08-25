
#Function to find Mid strings 
def findmidstr(a,b):
    print(f"Mid index of string '{a}' is {b//2} ")    
    if (b%2 != 0 ):
        print(f"First half slice of '{a}' is '{a[0:b//2]}'")
        print(f"Second half slice of '{a}' is {a[b//2:]}")
    else:
        print(f"First half slice of '{a}' is '{a[0:b//2]}'")
        print(f"Second half slice of '{a}' is '{a[b//2:]}'")

#Function to find the slice of strings
def slice_operation(a):
    b = int(len(a))
    print(f"Slice of '{a}' after removing first and last character '{a[1:-1]}'")
    print(f"Slice of '{a}' after removing first 2 character '{a[2:]}'")
    print(f"Slice of '{a}' after removing last 2 character '{a[:-2]}'")
    findmidstr(a,b)


#Accept input
print("Enter a String Value :")
a = (input())
print(f'You entered : {a} ')

slice_operation(a)
