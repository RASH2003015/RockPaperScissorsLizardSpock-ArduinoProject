
# import modules from Pyfirmata 
from pyfirmata import Arduino, util, INPUT, OUTPUT 
# import inbuilt time module

import time
# import random

from random import randrange



board = Arduino("com6")


it = util.Iterator(board) 
it.start()

choices = ["Rock", "Paper", "Scissor", "Spock", "Lizard", "EXIT"]


def u_choice(start_time = 0):

    start_time = start_time    #this start time is added for the timer()

    while True:

        now_time = time.time()
        timer(start_time, now_time)


        if board.digital[7].read() :
            return "Rock"
        elif board.digital[6].read() :
            return "Paper"
        elif board.digital[5].read() :
            return "Scissor"
        elif board.digital[4].read() :
            return "Spock"
        elif board.digital[3].read() :
            return "Lizard"
        elif board.digital[2].read() :
            return "EXIT"
    
def c_choice():    #Get computers choice randomly

    x = randrange(5)
    return choices[x]

def show_c_choice(computer):    #show computer's choice by lighting a bulb
    if computer == "Rock":
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
    
    elif computer == "Paper":
        board.digital[12].write(1)
        time.sleep(1)
        board.digital[12].write(0) 

    elif computer == "Scissor":
        board.digital[11].write(1)
        time.sleep(1)
        board.digital[11].write(0)

    elif computer == "Spock":
        board.digital[10].write(1)
        time.sleep(1)
        board.digital[10].write(0)      
    else:
        board.digital[9].write(1)
        time.sleep(1)
        board.digital[9].write(0)
    
    time.sleep(0.5)

def timer(start_time, now_time):   #Lights the bulbs according to the time
    
    if now_time - start_time <1:

        board.digital[13].write(1)  #computer's side
        board.digital[12].write(1)
        board.digital[11].write(1)
        board.digital[10].write(1)
        board.digital[9].write(1)
    
    elif now_time - start_time <2:

        board.digital[13].write(0)  #computer's side
        board.digital[12].write(1)
        board.digital[11].write(1)
        board.digital[10].write(1)
        board.digital[9].write(0)
    
    elif now_time - start_time <3:

        board.digital[13].write(0)  #computer's side
        board.digital[12].write(0)
        board.digital[11].write(1)
        board.digital[10].write(0)
        board.digital[9].write(0)

    else:
        board.digital[13].write(0)  #computer's side
        board.digital[12].write(0)
        board.digital[11].write(0)
        board.digital[10].write(0)
        board.digital[9].write(0)



def u_pin_input():    #make all the user pins as INPUTs

    board.digital[7].mode = INPUT
    board.digital[6].mode = INPUT
    board.digital[5].mode = INPUT
    board.digital[4].mode = INPUT
    board.digital[3].mode = INPUT
    board.digital[2].mode = INPUT

def u_pin_output():    #make all the user pins as OUTPUTs
    board.digital[7].mode = OUTPUT
    board.digital[6].mode = OUTPUT
    board.digital[5].mode = OUTPUT
    board.digital[4].mode = OUTPUT
    board.digital[3].mode = OUTPUT

def c_pin_output():    #make all the computer pins as OUTPUTs
    board.digital[13].mode = OUTPUT
    board.digital[12].mode = OUTPUT
    board.digital[11].mode = OUTPUT
    board.digital[10].mode = OUTPUT
    board.digital[9].mode = OUTPUT
    board.digital[8].mode = OUTPUT



def win(user, computer):    #decide who won the round

    if user == computer:
        return "TIE"
    
    elif user == "Spock":
        if computer == "Paper" or computer == "Lizard":
            return "LOSE"
        else:
            return "WIN"

    elif user == "Paper":
        if computer == "Scissor" or computer == "Lizard":
            return "LOSE"
        else:
            return "WIN"
        
    elif user == "Rock":
        if computer == "Paper" or computer == "Spock":
            return "LOSE"
        else:
            return "WIN"
        
    elif user == "Lizard":
        if computer == "Scissor" or computer == "Rock":
            return "LOSE"
        else:
            return "WIN"
    
    else:
        if computer == "Rock" or computer == "Spock":
            return "LOSE"
        else:
            return "WIN"

def show_score(score_1, score_2):       #show the scores by lighting bulbs
    binary_s_1 = '{0:03b}'.format(score_1)
    binary_s_2 = '{0:03b}'.format(score_2)

    u_pin_output()
    board.digital[7].write(int(binary_s_1[0]))  #user's side
    board.digital[6].write(int(binary_s_1[1]))
    board.digital[5].write(int(binary_s_1[2]))

    board.digital[13].write(int(binary_s_2[0]))  #computer's side
    board.digital[12].write(int(binary_s_2[1]))
    board.digital[11].write(int(binary_s_2[2]))
    
    print("u =", score_1, "C =", score_2)
    time.sleep(1)

def all_lights(i):      #to ON ar OFF all the bulbs

    u_pin_output()
    board.digital[7].write(i)  #user's side
    board.digital[6].write(i)
    board.digital[5].write(i)
    board.digital[4].write(i)
    board.digital[3].write(i)

    board.digital[13].write(i)  #computer's side
    board.digital[12].write(i)
    board.digital[11].write(i)
    board.digital[10].write(i)
    board.digital[9].write(i)
      
def buzzer():
    board.digital[8].write(1)
    time.sleep(1)
    board.digital[8].write(0)
    time.sleep(1)



def main():

    score_1 = 0
    score_2 = 0
    rounds = 0

    c_pin_output()
    u_pin_input()

    if u_choice() == "EXIT": # in here EXIT means START
                             # when the 6th button is pressed game begins

        all_lights(1)
        time.sleep(0.3)

        all_lights(0)
        time.sleep(0.3)

        all_lights(1)
        time.sleep(1)
        all_lights(0)
        time.sleep(2)



        while rounds <7 :

            u_pin_input()

            rounds = rounds + 1
            computer = c_choice()       
            start_time = time.time()
            user = u_choice(start_time)
          #  time.sleep(0.5)
            all_lights(0)
            time_def = time.time() - start_time

            time.sleep(0.5)

            show_c_choice(computer)

            print("U =", user, "C =", computer)

            if user == "EXIT" : #to exit
                show_score(score_1, score_2)
                all_lights(0)
                buzzer()
                return
            elif time_def >= 3: #for the 3 sec
                score_2 = score_2 + 1
                print("U have exceeded the given time.")
                
                show_score(score_1, score_2)
                all_lights(0)
                time.sleep(1)
                print()

            else:               #giving the score
                result = win(user, computer)

                if result == "WIN":
                    score_1 = score_1 + 1
                    print("User wins")

                elif result == "LOSE":
                    score_2 = score_2 + 1
                    print("User lose")

                else:
                    print("A Tie")
                
                show_score(score_1, score_2)
                time.sleep(0.5)
                all_lights(0)
                time.sleep(1)
                print()
        buzzer()  
        



while True:
    print("Start")
    main()














