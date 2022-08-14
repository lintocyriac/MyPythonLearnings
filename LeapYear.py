# Accept Input
def input_year():
    print("Enter the Input :")
    a = int(input())
    print(f'Checking if {a} is a Leap Year...')
    return a

# Check Whether the input is a Leap year
def leap_year(a):
    if(a%400 == 0):
        print(f'{a} is a Leap Year as it is divisible by 400.')
        print('Process finished with Exit Code 0.')
    elif(a%100 == 0):
        print(f'{a} is not a Leap Year as it is divisible by 100 but not by 400.')
        print('Process finished with Exit Code 0.')
    elif(a%4 == 0):
        print(f'{a} is a Leap Year as it is divisible by 4 but not by 100 or 400.')
        print('Process finished with Exit Code 0.')
    else:
        print(f'{a} is not a Leap Year as it is not divisible by 4.')
        print('Process finished with Exit Code 0.')

    
a= input_year()
leap_year(a)


