#Add function

def add(a,b):
    return a+b

#subtract function
def subtract(a,b):
    return a-b

#multiply function
def multiply(a,b):
    return a*b

#divide function
def divide(a,b):
    return float(a/b)

#remainder function
def remainder(a,b):
    return a%b

#Quotient function
def quotient(a,b):
    return a//b

#square function
def square(a):
    return a*a


# Print the Options
def options():
    
    print('***** Choose an option *****')
    print('**    (1) ADD             **')
    print('**    (2) Subtract        **')
    print('**    (3) Multiply        **')
    print('**    (4) Divide          **')
    print('**    (5) Find Remainder  **')
    print('**    (6) Find Quotient   **')
    print('**    (7) Find Square     **')
    print('**    (8) EXIT            **')
    print('****************************')
    return(int(input()))

#input number accept funcion

def input_num():
    print("Enter the first Number :")
    a = int(input())
    print("Enter the second Number :")
    b = int(input())
    return(a,b)

def checck_input():
    usr_entry = options()


    if (usr_entry==1):
        print('You have Entered Option (1) ADDITION')
        a,b = input_num()
        print(f'The sum of {a} and {b} is : {add(a,b)}')
        checck_input()

    elif(usr_entry==2):
        print('You have Entered Option (2) SUBTRACTION')
        a,b = input_num()
        print(f'The difference of {a} and {b} is : {subtract(a,b)}')
        checck_input()

    elif(usr_entry==3):
        print('You have Entered Option (3) MULTIPLICATION')
        a,b = input_num()
        print(f'The result of {a} times {b} is : {multiply(a,b)}')
        checck_input()

    elif(usr_entry==4):
        print('You have Entered Option (4) DIVISION')
        a,b = input_num()
        if(b==0):
            print('**Division by Zero is not possible.')
            print('Please enter a non-zero number :')
            b=int(input())
            print(f'The result of {a} divided by {b} is : {divide(a,b)}')
        else:
            print(f'The result of {a} divided by {b} is : {divide(a,b)}')
        checck_input()

    elif(usr_entry==5):
        print('You have Entered Option (5) REMAINDER')
        a,b = input_num()
        if(b==0):
            print('**Division by Zero is not possible.')
            print('Please enter a non-zero number :')
            b=int(input())
            print(f'The remainder of {a} divided by {b} is : {remainder(a,b)}')
        else:
            print(f'The remainder of {a} divided by {b} is : {remainder(a,b)}')
        checck_input()

    elif(usr_entry==6):
        print('You have Entered Option (6) QUOTIENT')
        a,b = input_num()
        if(b==0):
            print('**Division by Zero is not possible.')
            print('Please enter a non-zero number :')
            b=int(input())
            print(f'The quotient of {a} divided by {b} is : {quotient(a,b)}')
        else:
            print(f'The quotient of {a} divided by {b} is : {quotient(a,b)}')
        checck_input()


    elif(usr_entry==7):
        print('You have Entered Option (7) SQUARE')
        print('Please enter a number :')
        a=int(input())
        print(f'The square of {a} is : {square(a)}')
        checck_input()

    elif(usr_entry==8):
        print('You have Entered Option (8) EXIT')
        print('Exting Now...')
        exit
    else:
        print('**INVALID USER ENTRY')  
        checck_input()

    

checck_input()

