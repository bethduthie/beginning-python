choice = input('Type in one to add or two to multiply: ')

while not choice == 'one' and not choice == 'two':
    choice = input('Select one or two: ')


if choice == 'one':
    addition = input('Select two numbers to add together. First number: ')
    addition2 = input('Select two numbers to add together. Second number: ')
    try:
        addition = int(addition)
        addition2 = int(addition2)
        print(addition + addition2)
    except:
        print('Error! That wasn\'t a number. Please try again using digits, not words.')

if choice == 'two':
    multiply = input('Select two numbers to multiply. First number: ')
    multiply2 = input('Select two numbers to multiply. Second number: ')
    try:
        multiply = int(multiply)
        multiply2 = int(multiply2)
        print(multiply * multiply2)
    except:
        print('Error! That wasn\'t a number. Please try again using digits, not words.')



