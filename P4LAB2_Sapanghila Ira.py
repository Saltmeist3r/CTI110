first_integer = int(input())
second_integer = int(input())

if second_integer < first_integer:
    print('Second integer can\'t be less than the first.')
else:
    for i in range(first_integer, second_integer+1, 5):
        print(i, end=' ')
    print()