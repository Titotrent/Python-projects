# The code below allows the user to guess the programmers favourite color 3 times
favorite_color= "purple"
guess_count=1 # start of the while loop
guess_limit=3
while guess_count<=guess_limit:
    guess=input('Guess my favorite color: ')
    guess_count+=1 # this always come before the if statements
    if guess==favorite_color:
        print('Correct guess')
        break
else:
    print('You lost ')
    print('My favorite color is purple red
