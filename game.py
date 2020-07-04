import random as rd
import sys

Score = 0
Wicket = 0
Over = 0.0
No_of_player = 11
Run_Scored = 0
Playing =True



def check_wicket_or_add_run():
    global No_of_player
    global Score
    global Wicket

    if Run_Scored == 0:
        print("\nThats a wicket, ouch!!!")
        No_of_player -= 1
        Wicket +=1
    else:
        Score += Run_Scored 
        print(f"\nScore:\n{Run_Scored} added. Total is {Score}")
        print()

def ball_thrown():
    global Over
    global Run_Scored

    Run_Scored = rd.randint(0, 6)
    Over +=0.1

    check_wicket_or_add_run()
    check_over()
    can_continue()


def can_continue():
    if Wicket == 10:
        display_board()
        sys.exit("\nMatch Over...All wickets are taken")

def check_over():
    global Over 
    global totalOver
    if Over > totalOver:
        display_board()
        sys.exit("\nMax Over reached.") 
    elif(round(Over % 1,1) >= .6):
        Over += .4
        print(f"Next Over...{round(Over)}\n")
    else:
        print(f"{round(0.6 - round(Over % 1,1),1)} balls remaining..")
        print()

def display_board():
    print()
    print(f"******\nScore is: {Score} | Wicket: {Wicket} | Overs: {round(Over)} | No of player remained: {No_of_player}\n*****")
    print()

def play_game():
    global totalOver
    
    totalOver = int(input("Enter the number of Overs: "))
    while Playing:
        print("***Enter your Choice***")
        ch = input("1.Show Dashboard\n2.Throw the ball\n3.Exit\nEnter Your Choice: ")
        
        if ch == "1":
            display_board()
        elif ch == "2":
            ball_thrown()
        elif ch == "3":
            sys.exit("\n\nSee Your Next Time...")
        else:
            print("Wrong Choice, try again...")
 
if __name__ == "__main__":
    play_game()    

    
