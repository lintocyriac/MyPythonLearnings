print('Welcome to the Angry Goblin Hunt')
print('An award-winning game full of adventure and excitment (!)\n')
a =input('What is your name? ')
#print('\n')
print(f'\n{a}, do you think youcan find the goblin hiding in the kitchen cupboards?\n|_| |_| |_| |_| |_|\n')

while(True):
    x = int(input('Can you guess where the goblin is hiding? '))
    if x !=1:
        print('No, sorry. The goblin is still hiding somewhere.\n')
    else:
        print("Well done. You've found the gobblin.")
        break
print('Thank you for playing. Now get back to work!')
