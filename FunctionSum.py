#print('Sum of 650 and 550 is: ',650+550)
def fun_sum(a,b):
    return a+b

print("Enter the first Number :")
a = int(input())
print("Enter the second Number :")
b = int(input())
print('The sum of {0} and {1} is {2}'.format(a,b,fun_sum(a,b)) )

print('Adding 100  : ', fun_sum(fun_sum(a,b),100))
print('Adding 1000 : ', fun_sum(fun_sum(fun_sum(a,b),100) , 1000 ) )


