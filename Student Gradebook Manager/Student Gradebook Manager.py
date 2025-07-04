


student_grades0={}
active= True
while active:
    name=input("What is your first name: ")
    test_scores=[]

    print("Please  enter your scores in this order MATH/COMMS/EXCEL/CODABILITY: ")

    for i in range(4):
      score=input("Type your test score here: ")
      test_scores.append(score)

    student_grades0[name]=test_scores
    print(student_grades0)

    decision=input('Do you want to  fill scores for other students(yes/no): ')
    if decision.lower().strip()=="no":
        active= False

all_averages={}
sum_avg=0
for student_name,student_scores  in student_grades0.items():
   
   student_scores_int=[int(value) for value in student_scores]
   average=sum(student_scores_int)/len(student_scores_int)
   print(f"{student_name}'s average score is {average:.2f}")

#class average
   all_averages[student_name]=average
   sum_avg+=average
class_avg=sum_avg/len(student_grades0)
print(f'\nThe class average is: {class_avg:.2f}')
    
#highest scorer
highest_scorer=max(all_averages,key=all_averages.get)
print(f'Highest scorer is {highest_scorer} with a score of {all_averages[highest_scorer]:.2f}')


# print('--- ---')
# print('end of session')


