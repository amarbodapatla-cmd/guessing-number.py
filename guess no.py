import random
def is_integer(prompt='enter a secrete  number:'):
    while True:
        user_input=input(prompt)
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            return int(user_input)
        else:
            print('invalid input')
    
print('welcome to guessing the number')
a= is_integer('lowerlimit :')
b= is_integer('upperlimit :')
secrete_number = random.randint(a, b)
attempt = 0
while True:
    
    guess = is_integer(f'enter between {a} to {b}:')
    attempt += 1
    if guess < secrete_number:
        print('too high')
    elif guess > secrete_number:
        print('too low')
    else:
        print(f'correct guessing number is a secret_number:{guess}. Attempts:{attempt}')
        break


        

                                
                                
