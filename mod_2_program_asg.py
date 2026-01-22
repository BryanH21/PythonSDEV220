secret: int = 5
guess: int = 7

if guess == secret:
    print('just right')
elif guess < secret:
    print('too low')
else:
    print('too high')


'4.2'

small: bool = True
green: bool = False

if small and green:
    print('pea')
elif small and not green:
    print('cherry')
elif not small and green:
    print('watermelon')
else:
    print('pumpkin')

'6.1'

numbers: list = [3, 2, 1, 0]
for number in numbers:
    print(number)

'6.2'

guess_me: int = 7
number: int = 1 

while True: 
    if number < guess_me:
        print('too low')
    elif number > guess_me:
        print('oops')
        break
    elif number == guess_me:
        print('found it!')
        break
    
    number += 1

'6.3'

guess_me: int = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else: 
        print('Opps')
        break