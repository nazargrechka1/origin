import keyboard
import random
import time


print('Guess the number game, click 7 for more information or click enter for play')


while True:

    key = keyboard.read_key()

    if key == '7':

        print('The programme generates random integer from 0 to 100.')
        print('You have to guess it and you have only 5 attempts for it')
        break

    elif key == 'enter':
        print('Let`s play')
        break
    
time.sleep(1)

num =  random.randint(0 , 100)
attempts = 0
maxAttempts = 5


while attempts < maxAttempts:
     
    try: userInput = int(input('Write your number'))

    except ValueError:
        print('please enter valid number')
        continue

    attempts += 1

    if userInput > num:
            print ('less')
            continue
    
    elif userInput < num:
            print ('more')
            continue

    else: print ('equal')
    break

else: print('You lose')