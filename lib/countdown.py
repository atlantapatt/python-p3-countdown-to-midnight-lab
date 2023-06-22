import time
# your code goes here!

def countdown(integer):
    while 0 < integer:
        print(f'{integer} SECOND(S)!')
        integer -= 1
    if 0 == integer:
        print('HAPPY NEW YEAR!')

def countdown_with_sleep(integer):
    while 0 < integer:
        print(f'{integer} SECOND(S)!')
        integer -= 1
        time.sleep(1)
    if 0 == integer:
        print('HAPPY NEW YEAR!')

