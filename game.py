import random as rd
import sys

Score = 0
Wicket = 0
Over = 0.0
No_of_player = 11
Run_Scored = 0
no_of_teams =0
Playing =True
current_team = 0


def reset_stats():
    global Score, Wicket, Over, No_of_player,Run_Scored
    Score = 0
    Wicket = 0
    Over = 0.0
    No_of_player = 11
    Run_Scored = 0



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
    check_current_player()

def check_current_player():
    global current_team

    if check_wicket_or_add_run() and check_over() and can_continue() == -1:
        current_team = teams[current_team] + 1
        reset_stats()


def can_continue():
    if Wicket == 10:
        display_board()
        # sys.exit("\nMatch Over...All wickets are taken")
        return -1

def check_over():
    global Over 
    global totalOver
    if Over > totalOver:
        display_board()
        # sys.exit("\nMax Over reached.") 
        return -1
    elif(round(Over % 1,1) >= .6):
        Over += .4
        print(f"Next Over...{round(Over)}\n")
        return 1
    else:
        print(f"{round(0.6 - round(Over % 1,1),1)} balls remaining..")
        print()
        return 1

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
    global no_of_teams    

    no_of_teams = int(input("Enter the number of teams: "))

    teams = []
    for i in range (no_of_teams):
        teams.append(i)

    play_game()
