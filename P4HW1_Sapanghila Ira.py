print('#CTI-110\n#P4HW1- Score List\n#Sapanghila,Ira Chriel\n#April 6, 2023')
print('')
num_scores = int(input('How many scores would you like to enter? '))
score_list = []
for i in range(num_scores):
    valid_score = False
    while not valid_score:
        score = float(input('Enter score #{}: '.format(i+1)))
        if score < 0 or score > 100:
            print('\nINVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            valid_input = False
            while not valid_input:
                score = float(input('Enter score #{} again: '.format(i+1)))
                if score < 0 or score > 100:
                    print('\nINVALID Score entered!!!!')
                    print('Score should be between 0 and 100')
                else:
                    valid_input = True
                    valid_score = True
                    score_list.append(score)
        else:
            valid_score = True
            score_list.append(score)
            
lowest_score = min(score_list)

modified_list = [score for score in score_list if score != lowest_score]

average_score = sum(modified_list) / len(modified_list)

if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print('')
print('--------------Results-----------')
print('Lowest score   : {:.1f}'.format(lowest_score))
print('Modified List  : {}'.format(modified_list))
print('Scores Average : {:.2f}'.format(average_score))
print('Grade          : {}'.format(letter_grade))
print('----------------------------------')

