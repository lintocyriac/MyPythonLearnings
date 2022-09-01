#Function to find Fibanacci numbers

def fib(a, count):
    first, second = 0, 1
    n = 0
    
    while(first < a):
        #print(first)
        fib = first + second
        first = second
        second = fib
        
    if (first > 1): 
        
            if(first > a):
                while(n < count):
                    print(first)
                    fib = first + second
                    first = second
                    second = fib            
                    n += 1
            else: 
                while(n < count):
                    print(second)               
                    fib = first + second
                    first = second
                    second = fib                             
                    n += 1
    elif(first == 1 ):
        while(n < count):
            fib = first + second
            first = second
            second = fib
            print(second)
            n += 1
    else:
        first = 1
        second =2
        while(n < count):
            print(first)
            fib = first + second
            first = second
            second = fib            
            n += 1


#Function to find odd numbers
     
def odd(a, count):
    print(f'Printing {count} odd numbers after {a}')
    if(a%2==0):
        a= a+1
        while count>0:
            print(a)
            a+=2
            count-=1
    else:
        while count>0:
            a+=2
            print(a)            
            count-=1

#Function to find even numbers
     
def even(a, count):
    print(f'Printing {count} even numbers after {a}')
    if(a%2==0):
        while count>0:
            a+=2
            print(a)
            count-=1
    else:
        a+=1
        while count>0:
            print(a)
            a+=2
            count-=1
#Accept input
while True:
    print('Enter a Number :')
    a = int (input())
    print(f'You entered  <{a}> ')
    print('What do you wish to print?')
    print('Choose one of the following option')
    print('********************\n')
    print(' (1) ODD NUMBERS')
    print(' (2) EVEN NUMBERS')
    print(' (3) FIBONACCI NUMBERS')
    print(' (0) EXIT\n')
    print('********************\n')
    b = int (input())

    if (b==1):
        print(f'You have entered Option 1 - ODD NUMBER')
        print('How many odd numbers you wish to print?')
        count = int (input())
        odd(a,count)

    elif (b==2):
        print(f'You have entered Option 2 - EVEN NUMBER\n')
        print('How many even numbers you wish to print?')
        count = int (input())
        even(a,count)

    elif (b==3):
        print(f'You have entered Option 3 - FIBONACCI NUMBERS\n')
        print('How many FIBONACCI NUMBERS you wish to print?')
        count = int (input())
        fib(a,count)

    elif (b==0):
        print(f'You have entered Option 4 - EXIT\n')
        print('EXITING NOW...')
        exit()
    else:
        print(f'Option {b} not on the list :(\n')
        print('Please enter a Valid Option')