import random as rd
import sys
# Global Variables

# List of number of teams
Teams = []
current_team = 0
index = 0
# Score 
Score = []
Run_Tracker = [current_team][index]
run = 0
Run_Scored = 0

#Wicket
Wicket = []
No_of_Wickets_Remaining = []

#Over
Over = []

# Main Function
def play_game():
    # For keeping the loop infinitely
    Playing =True
    # Do While Loop
    while Playing:
        
        print("\n********************************************************************\n")
        ch = input("1.Show Dashboard for current Team\n2.Show Dashboard for all Teams\n3.Show the Run Tracker\n4.Throw the ball\n5.Exit\nEnter Your Choice: ")
        print("\n********************************************************************\n")
        # Switch Case 
        if ch == "1":
            display_board_for_current_player()
        elif ch == "2":
            display_board()
        elif ch=="3":
            display_run_tracker()
        elif ch == "4":
            ball_thrown()
        elif ch == "5":
            sys.exit("\nSee Your Next Time...\n")
        else:
            print("Wrong Choice, try again...")   

# Display For all team
def display_board():
    for i in range(no_of_teams):
        print()
        print(f"******\nDashbord for team {i+1}")
        print(f"Score is: {Score[i]} | Wicket: {Wicket[i]} | Overs: {round(Over[i],1)} | No of player remained: {No_of_Wickets_Remaining[i]}\n******")
        print()
#display for current player only
def display_board_for_current_player():
        print()
        print(f"******\nDashbord for team {current_team+1}")
        print(f"Score is: {Score[current_team]} | Wicket: {Wicket[current_team]} | Overs: {round(Over[current_team],1)} | No of player remained: {No_of_Wickets_Remaining[current_team]}\n******")
  
        print()

# Not Working

def display_run_tracker():
    # score = []
    # print(f"Runs for the Team {current_team + 1}: ")
    # for i in range(len(Run_Tracker[current_team])-1):
    #     print(f"{i}" + ", ")[:-2]
    # for i in range(index): 
    #     score.append(Run_Tracker[current_team][i]) # +  ", "

    # print(score)
    # for i in score:
    #     print(i)[:-1]
    pass

# Game Start here
def ball_thrown():
    global Over,Run_Scored,current_team
    
    #Randmonly Generate a Value Betwwen 0 and 6 for the runs
    Run_Scored = rd.randint(0, 6)
    #Iterating Over
    Over[current_team] +=0.1
    #checking condition
    check_run()
    check_wicket()
    
    if check_over() == "over":
        print(f"\nMax Over limit reached of {round(Over[current_team])}\n")
        check_current_team() 
        

def check_run():
    global No_of_Wickets_Remaining, run, Wicket,current_team, index, Run_Tracker
    # When score is 0, Player is Out
    if Run_Scored == 0:
        print("\nThats a wicket, ouch!!!")
        No_of_Wickets_Remaining[current_team] -= 1
        Wicket[current_team] +=1
    #Else Runs Are Added To the Score
    else:
        run += Run_Scored 
        #Tracking the Runs
        if Run_Scored == 0:
            Run_Tracker = "W"
        else:
            Run_Tracker = Run_Scored
        index += 1
        #Fixed where score was not added in runtime
        Score[current_team] =run
        print(f"Score:\n{Run_Scored} added. Total is {run}")

#Number of Over Are Checked
def check_over():
    global Over, totalOver,current_team
    
    #value = Over % 1 
    #This gives the decimal place value
    #Then Rounded using Round Func
    #Round(value,round till this decimal place)
    if(round(Over[current_team] % 1,1) >= .6):
        #Since Over are of 6 balls, Remaning are adjusted
        Over[current_team] += .4 
        if Over[current_team] > totalOver:
            return "over"
        print(f"Over {round(Over[current_team])} finished\n")
    else:
        #Print the remaining Balls in the over
        print(f"{round(0.6 - round(Over[current_team] % 1,1),1)} balls remaining..")
        print()

#Checks Wicket
def check_wicket():
    if Wicket == 10:
        display_board()
        check_current_team()

#Check Current Player
def check_current_team():
    global current_team, run
    #Check the Return Value
    check_winner()
    display_board_for_current_player()
    current_team += 1
    run =0
    # Score.append(run)
    print(f"### TEAM CHANGE TO TEAM {current_team +1} ###")
    # reset_stats()

def check_winner():
    global Score, Teams, current_team
    #winner checker
    winner_score = Score[0]
    winner = Teams[0] 
    #check if the last team is playing
    if Teams[current_team] == len(Teams)-1:
        display_board()
        for i in  range(len(Teams)-1):
            if Score[i+1] >= winner_score:
                winner_score = Score[i+1]
                winner = Teams[i+1]

        for i in range(len(Teams)-1):
            for j in range(len(Teams)-1):
                if Score[i] == Score[j+1]:
                    print(f"Tied Between {Teams[i+1]} and {Teams[j+1]} ")
            break
        print(f"*********\n\nTeam {winner +1} Wins the match with the score of {winner_score}. Congrats\n*********")
        sys.exit("Thanks for playing...\n")
    else: print(f"### TEAM {current_team+1} CHANGE OVER ###")

#  Execution start from here
if __name__ == "__main__":

    no_of_teams = int(input("Enter the number of Teams: "))
    totalOver = int(input("\nEnter the number of Overs: "))
    totalOver -= 1
    #  To over come index out of range
    for i in range (no_of_teams):
        Teams.append(i)
        Score.append(0)
        Wicket.append(0)
        Over.append(0)
        No_of_Wickets_Remaining.append(10)

    display_board()
    play_game()
