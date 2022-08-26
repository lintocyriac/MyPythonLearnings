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
print('Enter a Number :')
a = int (input())
print(f'You entered  <{a}> ')
print('What do you wish to print?')
print('Choose one of the following option')
print('********************\n')
print(' (1) ODD NUMBER')
print(' (2) EVEN NUMBER\n')
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

else:
    print(f'Option {b} not on the list :(\n')
    print('Exiting Now......')
    
