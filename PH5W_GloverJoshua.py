# Home work
# 06DEC2023
# CTI-110 P5HW - Math Quiz
# Glover, Joshua
#

# Have the program generate random numbers



# create Menu Page


def menu():
    global menu
    print('MAIN MENU')
    print('--------------------')
    print("[1] Adding Random Numbers")
    print("[2] Subtracting Random Numbers")
    print("[3] Exit")

menu()

import random

while True:
    option = int(input('Please choose from one of the menu options: '))

    if option == 1:
        num_1 = random.randint(1, 234)
        num_2 = random.randint(1, 234)
        
        print(num_1)
        print("+", num_2)

       
        
        while True:
            right_answer = num_1 + num_2
            user_answer = int(input())
            
        
            if user_answer == right_answer:
                print('Congratulations')
                print('Number of guesses: ')
                break
                
                option = int(input('Please choose from one of the menu options: '))
                
            


            elif user_answer < right_answer:
                print('Too low')

            else:
                user_answer > right_answer
                print('Too high')

                
         
                
            
    elif option == 2:
        num_1 = random.randint(1, 234)
        num_2 = random.randint(1, 234)

        print(num_1)
        print('-', num_2)

        i = 0
        while i == 0:
            i = i + 1


        while True:
            right_answer = num_1 - num_2
            user_answer = int(input())
            if user_answer == right_answer:
                print('Congratulations')
                print('Number of guesses: ', i)
                
                break


            elif user_answer < right_answer:
                print('Too low')

            else:
                user_answer > right_answer
                print('Too high')
                
            



            
    elif option == 3:
        print('Thank you for playing...')
        print('Bye')
        break

    
    else:
        print('Invalid Option')




