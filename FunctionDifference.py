print('######## FINDING THE ABSOLUTE DIFFERNCE BETWEEN TWO NUMBERS USING FUNCTION #########')

# Define a function to get the difference
def fun_diff(a,b):
    return a-b

#Accept input as integer
print("Enter the first Number :")
a = int(input())
print("Enter the second Number :")
b = int(input())

#Difference @entering order
print('The difference of {0} and {1} is {2}'.format(a,b,fun_diff(a,b)) )

#Finding the Absolute difference
if (a>b):
    print('The Absolute difference of {0} and {1} is {2}'.format(a,b,fun_diff(a,b) ))
else:
    print('The Absolute difference of {0} and {1} is {2}'.format(a,b,fun_diff(b,a) ))

