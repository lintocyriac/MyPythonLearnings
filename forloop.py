#Function to print the characters in a string left - ringht order
def print_operation(a):
    #b = int(len(a))
    #count =0
    for i in a:
        print(i)
        
#Function to print the characters in a string reverse order       
def print_operationRev(a):
    str=""
    for i in a:
        str = i + str
    print_operation(str)   

#Accept input
print("Enter a String Value :")
a = (input())
print(f'You entered : {a} ')
print(f'Print character of <{a}>  \n')
print_operation(a)
print(f'Print character of <{a}> in reverse \n')
print_operationRev(a)