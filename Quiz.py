# The program below is quiz made by python. The answers are fixed.
name= input('What is your name? ' )
print(f'{name}, the quiz below consists of 4 questions.')
choice=input('Are you ready to take the test? ')
if choice.lower()!='yes':
    quit()
score=0
print('Qstn 1:How many seasons are there on earth? ')
answer=input('')
if answer.lower()=='4':
    print('Correct')
    score+=2
else:
    print('Incorrect')
print('Qstn 2:What are two things you can never eat for breakfast? ')
answer=input('')
if answer.lower()=='lunch and supper':
    print('Correct')
    score+=2
else:
    print('Incorrect')
    print('Answer:Lunch and supper')
print('Qstn 3:How do you make the number one disappear? ')
answer = input('')
if answer.lower() == 'add a g':
        print('Correct')
        score += 2
else:
        print('Incorrect')
        print('Answer: Add a g to make it gone')
print('Qstn 4:What is your name ? ')
answer=input('')
if answer.lower()==name.lower():
    print('Correct')
    score+=2
else:
    print('Incorrect')
print('Your score is ',((score/8)*100),'%' )

