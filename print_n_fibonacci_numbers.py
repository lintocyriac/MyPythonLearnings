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



#Accept input
print('Enter a Number :')
a = int (input())
print(f'You entered  <{a}> ')
print('How many fibonacci numbers you wish to print?')
count = int (input())
print(f'Printing {count} fibonacci numbers after {a} :')


fib(a, count)

