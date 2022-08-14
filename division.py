
#Accept inputs
print("Enter the first Number :")
a = int(input())
print("Enter the second Number :")
b = int(input())


#Check whether the second number is zero then its not a valid number to divide
if(b==0):
    print("Division by Zero is not possible")
elif b<0:
    print('Number not Accepted. Please Rerun the program and enter a positive number')       
else:
    print('Both Numbers are valid')
    print('The result of {0} divided by {1} is {2}'.format(a,b,float(a/b) ))
    


