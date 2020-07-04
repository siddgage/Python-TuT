import random as rd
import sys

teams = []
current_team = 1

Score = []
run = 0

Wicket = []
Over = []
No_of_player = []

Run_Scored = 0
Playing =True

def play_game():
    while Playing:
        
        print("\n********************************************************************\n")
        ch = input("1.Show Dashboard\n2.Throw the ball\n3.Exit\nEnter Your Choice: ")
        print("\n********************************************************************\n")
        
        if ch == "1":
            display_board()
        elif ch == "2":
            ball_thrown()
        elif ch == "3":
            sys.exit("\n\nSee Your Next Time...")
        else:
            print("Wrong Choice, try again...")   

def display_board_for_first_time():
    for i in range(no_of_teams):
        print()
        print(f"******\nDashbord for team {i+1}")
        print(f"Score is: {Score[i]} | Wicket: {Wicket[i]} | Overs: {round(Over[i])} | No of player remained: {No_of_player[i]}\n******")
        print()

def display_board():
    global no_of_teams, current_team
    for i in range(no_of_teams):
        print()
        print(f"******\nDashbord for team {i+1}")
        print(f"Score is: {Score[current_team]} | Wicket: {Wicket[current_team]} | Overs: {round(Over[current_team])} | No of player remained: {No_of_player[current_team]}\n******")
        print()


def ball_thrown():
    global Over,Run_Scored,current_team

    Run_Scored = rd.randint(0, 6)
    Over[current_team] +=0.1
    
    check_wicket_or_add_run()
    check_over()
    can_continue()

def check_wicket_or_add_run():
    global No_of_player, run, Wicket,current_team

    if Run_Scored == 0:
        print("\nThats a wicket, ouch!!!")
        No_of_player[current_team] -= 1
        Wicket[current_team] +=1
    else:
        run += Run_Scored 
        print(f"\nScore:\n{Run_Scored} added. Total is {run}")
        print()

def check_over():
    global Over, totalOver,current_team
    if Over[current_team] > totalOver:
        display_board()
        # sys.exit("\nMax Over reached.") 
        return -1
    elif(round(Over[current_team] % 1,1) >= .6):
        Over[current_team] += .4
        print(f"Next Over...{round(Over[current_team])}\n")
        return 1
    else:
        print(f"{round(0.6 - round(Over[current_team] % 1,1),1)} balls remaining..")
        print()
        return 1

def can_continue():
    if Wicket == 10:
        display_board()
        # sys.exit("\nMatch Over...All wickets are taken")
        return -1
    else: return 1


def check_current_player():
    global current_team, teams, Score, run

    winner = teams[1] 
    if check_over() and can_continue() == 1:
        pass
    elif current_team == len(teams) -1:
        for i in  range(no_of_teams):
            if Score[i+2] > Score[i+1]:
                winner = teams[i+2]
                if Score[i+2] == Score[i+1]:
                    print(f"Tied Between {teams[i] +1} and {teams[i+1] +1} ")
                else: continue
        print(f"*********\n\nTeam {winner} Wins the match. Congrats\n\n*********")
        sys.exit("Thanks for playing...\n")
    elif check_over() and can_continue() == -1:
        current_team += 1
        Score.append(run)
        print(f"PLAYER CHANGE TO TEAM {current_team}")
        # reset_stats()



# def reset_stats():
#     global run, Wicket, Over, No_of_player,Run_Scored
#     run = 0
#     Wicket = 0
#     Over = 0.0
#     No_of_player = 11
#     Run_Scored = 0


if __name__ == "__main__":

    no_of_teams = int(input("Enter the number of teams: "))
    totalOver = int(input("\nEnter the number of Overs: "))
    for i in range (no_of_teams):
        teams.append(i+1)
        Score.append(0)
        Wicket.append(0)
        Over.append(0)
        No_of_player.append(11)

    display_board_for_first_time()
    play_game()
