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
        print(f"******\nDashbord for team {current_team+1}")
        print(f"Score is: {Score[current_team]} | Wicket: {Wicket[current_team]} | Overs: {round(Over[current_team])} | No of player remained: {No_of_teams[current_team]}\n******")
        print()


# Game Start here
def ball_thrown():
    global Over,Run_Scored,current_team
    
    #Randmonly Generate a Value Betwwen 0 and 6 for the runs
    Run_Scored = rd.randint(0, 6)
    #Iterating Over
    Over[current_team] +=0.1
    #checking condition
    if check_over() == "over":
        pass
    else: 
        check_wicket_or_add_run()
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
        print(f"Score:\n{Run_Scored} added. Total is {run}")

#Number of Over Are Checked
def check_over():
    global Over, totalOver,current_team
    if Over[current_team] > totalOver:
        # sys.exit("\nMax Over reached.") 
        check_current_team()
        return "over"
    #value = Over % 1 
    #This gives the decimal place value
    #Then Rounded using Round Func
    #Round(value,round till this decimal place)
    elif(round(Over[current_team] % 1,1) >= .6):
        #Since Over are of 6 balls, Remaning are adjusted
        Over[current_team] += .4 
        print(f"Next Over...{round(Over[current_team])}\n")
    else:
        #Print the remaining Balls in the over
        print(f"{round(0.6 - round(Over[current_team] % 1,1),1)} balls remaining..")
        print()

#Checks Wicket
def can_continue():
    if Wicket == 10:
        display_board()
        # sys.exit("\nMatch Over...All wickets are taken")
        check_current_team()
    else: pass

#Check Current Player
def check_current_team():
    global current_team, run
    #Check the Return Value
    check_winner()
    display_board_for_current_player()
    current_team += 1
    run =0
    # Score.append(run)
    print(f"TEAM CHANGE TO TEAM {current_team +1}")
    # reset_stats()

def check_winner():
    global Score, teams, current_team
    #winner checker
    winner_score = 0
    winner = teams[0] 
    #check if the last team is playing
    if teams[current_team] == len(teams)-1:
        for i in  range(len(teams)-1):
            if Score[i+1] >= winner_score:
                winner_score = Score[i+1]
                winner = teams[i+1]
                # if Score[i+1] == Score[i]:
                #     print(f"Tied Between {teams[i]} and {teams[i+11]} ")
        display_board()
        print(f"*********\n\nTeam {winner +1} Wins the match with the score of {winner_score}. Congrats\n\n*********")
        sys.exit("Thanks for playing...\n")
    else: print(f"Team {current_team+1} chance is over")

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
