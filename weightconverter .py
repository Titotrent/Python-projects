name=input('What is your name? ')
weight=int(input(f'{name},what is your weight? ' ))#use of formated strings.
option=input('(L)bs or (K)gs: ')
if option.upper()=='L':
    converted_weight=round(weight*0.453592)
    print('You are ', converted_weight,'kgs' )
else:
    converted_weight=round(weight/0.453592)
    print('You are ',converted_weight ,'lbs')