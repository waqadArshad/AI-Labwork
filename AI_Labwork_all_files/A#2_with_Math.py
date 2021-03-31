import math
import random

# Let's make something useful.

Name = input("What is your name? ")
print("Hello Mr. {}".format(Name))
print("Let's predict which team has more chances (or how many chances) to win!")
team1 = input("Please enter the name of 1st team: ")
print("Now you will have to put the statistics (won/lost matches) of team {} to predict their win!".format(team1))

print("------------------------**-----------|-----------------------------------------------------")
print("----------------------**-*---****--**|**---------------------------------------------------")
print("-------------------------|---|***----|-----------------------------------------------------")
print("-----------------------****--***|----|****-------------------------------------------------")

totalMatches_team1 = input("Please enter the total matches played by " + team1 + ": ")
matchesWon_team1 = input("Please enter the matches won by " + team1 + " out of "
                         + totalMatches_team1 + " matches: ")
matchesLost_team1 = input("Please enter the matches lost by " + team1 + " out of "
                          + totalMatches_team1 + " matches: ")
matchesTied_team1 = input("Please enter the matches that got tied out of "
                          + totalMatches_team1 + " matches: ")
team1_winPercentage = (((float(matchesWon_team1) + float(matchesTied_team1) +
                         float((random.randint(1, 50)) / (random.randint(1, 30)))) /
                        float(totalMatches_team1)) * 100)
# print(team1_winPercentage)
# print(round(team1_winPercentage, 4))
team1_winPercentageRounded = round(team1_winPercentage, 4)
print("Rounded percentage for Team-1 is: {}".format(team1_winPercentageRounded))
team1_winPercentageCeil = math.ceil(team1_winPercentageRounded)
# print(team1_winPercentageCeil)
# print(team1_winPercentage)

print("-----------------------***----------------*-------------------------------------------------")
print("--------------------------*---------------*-------------------------------------------------")
print("--------------------------*---***-*---*****-------------------------------------------------")
print("-----------------------****--|---|----|****-------------------------------------------------")

team2 = input("Please enter the name of 2nd team:  ")
print("Now you will have to put the statistics (won/lost matches) of team {} to predict their win!".format(team1))
totalMatches_team2 = input("Please enter the total matches played by " + team2 + ": ")
matchesWon_team2 = input("Please enter the matches won by " + team2 + " out of "
                         + totalMatches_team2 + " matches: ")
matchesLost_team2 = input("Please enter the matches lost by " + team2 + " out of "
                          + totalMatches_team2 + " matches: ")
matchesTied_team2 = input("Please enter the matches that got tied out of "
                          + totalMatches_team2 + " matches: ")
team2_winPercentage = (((float(matchesWon_team2) + float(matchesTied_team2) +
                         float((random.randint(1, 50)) / (random.randint(1, 30)))) /
                        float(totalMatches_team2)) * 100)
team2_winPercentageRounded = round(team2_winPercentage, 4)
print("Rounded percentage for Team-2 is: {}".format(team2_winPercentageRounded))
team2_winPercentageCeil = math.ceil(team2_winPercentageRounded)
# print(team2_winPercentageCeil)
# print(team2_winPercentage)

if team1_winPercentageCeil > team2_winPercentageCeil:
    team1_winPercentageCeil += float(((len(team1)+team1.count('s'))*random.randint(1, 50))/100)
    if team1_winPercentageCeil <= 100:
        print("\n\nFrom the given data my algorithm concludes that, {} has {}% chances of winning which is more than {}. "
          .format(team1.title(), team1_winPercentageCeil, team2.capitalize()))
    else:
        print("\n\nFrom the given data my algorithm concludes that, {} has {}% chances of winning which is more than {}. "
            .format(team1.title(), 100, team2.capitalize()))

else:
    team2_winPercentageCeil += float(((len(team2)+team2.count('a')) * random.randint(1, 50)) / 100)
    if team2_winPercentageCeil <= 100:
        print("\n\nFrom the given data my algorithm concludes that, {} has {}% chances of winning which is more than {}. "
          .format(team2.title(), team2_winPercentageCeil, team1.capitalize()))
    else:
        print("\n\nFrom the given data my algorithm concludes that, {} has {}% chances of winning which is more than {}. "
            .format(team2.title(), 100, team1.capitalize()))
    print("\n\nFrom the given data my algorithm concludes that, {} has {}% chances of winning which is more than {}. "
          .format(team2.title(), team2_winPercentageCeil, team1.capitalize()))

# print("\n\nFrom the given data my algorithm concludes that, {} has {}% chances of winning and "
#       "{} has {}% chances of winning".format(team1, team1_winPercentageCeil, team2, team2_winPercentageCeil))
