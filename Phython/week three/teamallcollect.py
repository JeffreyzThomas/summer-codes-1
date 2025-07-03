

import random # Import the random module

# Create a list of players stored in the players variable
players = ["Avery", "Kamari", "Max",
           "Jeffery", "Braylen", "Xavier",
           "Carl", "Walter", "Darren",
           "EJ", "Nahum", "Joaquin",
           "Marshawn", "Ja 'Den", "Isaiah",
           "Kriss", "Joseph", "Semaj",
           "Tay", "Taqari", "Kauri",
           "Kenlon", "Nishad", "Jarmauri"]

def allocateTeams(players):         # Create a function
    random.shuffle(players)       # Shuffle the list of players
    team1 = players[:len(players) // 2]       # Put the first half of the players in team1
    teamCaptain1 = team1 [random.randrange(0, 12)]       # Randomly select a team captain from team1
  
    print("TEAM 1:")
    print ("Team 1 Captain: " + teamCaptain1)
    for player in team1:
        print(player)

team2 = players[len(players) // 2:]
teamcaptian2 = team2 [random.randrange(0, 12)]

print("TEAM 2")
print("Team 2 captain: " + teamcaptian2)
for player in team2:
    print(player)


allocateTeams(players)

 #a collection of python moduals 
#input comand 
#maths webroswer
#a python file 
#It helps sort and mannage tasks, its like half the work is done 