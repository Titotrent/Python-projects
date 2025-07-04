


student_grades0 = {}
active = True

while active:
    student_name = input("What's your name: ")

    test_scores = []
    subjects = ['Math', 'English', 'Python', 'Excel']

    print('\nEnter your scores below:')
    for subject in subjects:
        while True:
            try:
                score = int(input(f'\t{subject} score: '))
                if 0 <= score <= 100:
                    test_scores.append(score)
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    student_grades0[student_name] = test_scores

    print('\nCurrent student scores:')
    print(student_grades0)

    decision = input('Do you want to continue filling in scores? (yes/no): ')
    if decision.lower().strip() == 'no':
        active = False

# Calculate averages
all_averages = {}
sum_avg = 0

print("\nIndividual Averages:")
for student_name, scores in student_grades0.items():
    average = sum(scores) / len(scores)
    all_averages[student_name] = average
    sum_avg += average
    print(f"{student_name}'s average score is {average:.2f}")

# Class average
class_avg = sum_avg / len(student_grades0)
print(f'\nThe class average is: {class_avg:.2f}')

# Highest scorer
highest_scorer = max(all_averages, key=all_averages.get)
print(f'\nHighest scorer is {highest_scorer} with a score of {all_averages[highest_scorer]:.2f}')

