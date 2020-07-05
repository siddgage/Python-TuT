import random as rd
import sys
# Global Variables

# List of number of teams
teams = []
current_team = 0

# Score Made
Score = []
run = 0

Wicket = []
Over = []
No_of_teams = []

Run_Scored = 0
# For keeping the loop infinitely
Playing =True

# Main Function
def play_game():
# Do While Loop
    while Playing:
        
        print("\n********************************************************************\n")
        ch = input("1.Show Dashboard for current team\n2.Show Dashboard for all teams\n3.Throw the ball\n4.Exit\nEnter Your Choice: ")
        print("\n********************************************************************\n")
    # Switch Case 
        if ch == "1":
            display_board_for_current_player()
        elif ch == "2":
            display_board()
        elif ch == "3":
            ball_thrown()
        elif ch == "4":
            sys.exit("\nSee Your Next Time...\n")
        else:
            print("Wrong Choice, try again...")   

# Display For all team
def display_board():
    for i in range(no_of_teams):
        print()
        print(f"******\nDashbord for team {i+1}")
        print(f"Score is: {Score[i]} | Wicket: {Wicket[i]} | Overs: {round(Over[i])} | No of player remained: {No_of_teams[i]}\n******")
        print()
#display for current player only
def display_board_for_current_player():
        print()
        print(f"******\nDashbord for team {current_team}")
        print(f"Score is: {Score[current_team]} | Wicket: {Wicket[current_team]} | Overs: {round(Over[current_team])} | No of player remained: {No_of_teams[current_team]}\n******")
        print()


# Game Start here
def ball_thrown():
    global Over,Run_Scored,current_team
    #Randmonly Generate a Value Betwwen 0 and 6 for the runs
    Run_Scored = rd.randint(0, 6)
    #Iterating Over
    Over[current_team] +=0.1
    #Checking Conditions 
    check_wicket_or_add_run()
    check_over()
    can_continue()

def check_wicket_or_add_run():
    global No_of_teams, run, Wicket,current_team
    # When score is 0, Player is Out
    if Run_Scored == 0:
        print("\nThats a wicket, ouch!!!")
        No_of_teams[current_team] -= 1
        Wicket[current_team] +=1
    #Else Runs Are Added To the Score
    else:
        run += Run_Scored 
        #Fixed where score was not added in runtime
        Score[current_team] =run
        print(f"\nScore:\n{Run_Scored} added. Total is {run}")

#Number of Over Are Checked
def check_over():
    global Over, totalOver,current_team
    if Over[current_team] > totalOver:
        display_board_for_current_player()
        # sys.exit("\nMax Over reached.") 
        return -1
    #value = Over % 1 
    #This gives the decimal place value
    #Then Rounded using Round Func
    #Round(value,round till this decimal place)
    elif(round(Over[current_team] % 1,1) >= .6):
        #Since Over are of 6 balls, Remaning are adjusted
        Over[current_team] += .4 
        print(f"Next Over...{round(Over[current_team])}\n")
        return 1
    else:
        #Print the remaining Balls in the over
        print(f"{round(0.6 - round(Over[current_team] % 1,1),1)} balls remaining..")
        print()
        return 1

#Checks Wicket
def can_continue():
    if Wicket == 10:
        display_board()
        # sys.exit("\nMatch Over...All wickets are taken")
        return -1
    else: return 1

#Check Current Player
def check_current_player():
    global current_team
    #Check the Return Value
    if check_over() and can_continue() == 1:
        pass
    elif check_over() and can_continue() == -1:
        current_team += 1
        # Score.append(run)
        print(f"PLAYER CHANGE TO TEAM {current_team}")
       # reset_stats()

def check_winner():
    global Score, teams, current_team
    #check if the last team is playing
    winner = teams[0] 
    if teams[current_team] == teams[no_of_teams-1]:
        for i in  range(no_of_teams):
            if Score[i+1] > Score[i]:
                winner = teams[i+1]
                if Score[i+1] == Score[i]:
                    print(f"Tied Between {teams[i +1]} and {teams[i+2]} ")
        print(f"*********\n\nTeam {winner} Wins the match. Congrats\n\n*********")
        sys.exit("Thanks for playing...\n")
    else: pass
                    
  


# def reset_stats():
#     global run, Wicket, Over, No_of_teams,Run_Scored
#     run = 0
#     Wicket = 0
#     Over = 0.0
#     No_of_teams = 11
#     Run_Scored = 0

#  Execution start from here

if __name__ == "__main__":

    no_of_teams = int(input("Enter the number of teams: "))
    totalOver = int(input("\nEnter the number of Overs: "))
#  To over come index out of range
    for i in range (no_of_teams):
        teams.append(i)
        Score.append(0)
        Wicket.append(0)
        Over.append(0)
        No_of_teams.append(11)

    display_board()
    play_game()
