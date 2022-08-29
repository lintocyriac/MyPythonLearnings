#Function to print characters in a string of strings
def print_operation(a):
    b = int(len(a))
    count =0
    while count < b:
        print(a[count])
        count=count +1

def char_int(a):
    a = a.lower().strip().replace(' ','')
    for i in range(0,len(a)):
        print(ord(a[i])-96, end = " ")     

#Accept input
print("Enter a String Value :")
a = (input())
print(f'You entered : {a} ')
print(f'Print character of <{a}>  \n')
print_operation(a)
char_int(a)
