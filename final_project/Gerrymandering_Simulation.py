#Gerrymandering Simulation
#By Wayne Tobias and Ed Hawkins

import random

districts = 3
districtVoters = 500
totalRepublicanVotes = 0
totalDemocratVotes = 0
totalElectionTrials = 5
totalDemocratWins = 0
totalRepublicanWins = 0
elections = 0
districtVoters = int(input("How many voters are in each district? "))
districts = int(input("How many districts would you like to create? "))
totalElectionTrials = int(input("How many elections would you like to run? "))
while elections < totalElectionTrials:
    democraticDistricts = 0
    republicanDistricts = 0
    i=0
    while i < districts - 1:
        democratVotes = 0
        republicanVotes = 0
        j = 0
        while j < districtVoters:
            if random.randint(1, 100) < 51:
                democratVotes += 1
            else:
                republicanVotes += 1
            j += 1
    
        if democratVotes > republicanVotes:
            democraticDistricts += 1
        else:
            republicanDistricts += 1
        totalDemocratVotes += democratVotes
        totalRepublicanVotes += republicanVotes
        i += 1

    democratTieVotes = districts * districtVoters - totalDemocratVotes
    republicanTieVotes = districts * districtVoters - totalRepublicanVotes

    if democratTieVotes > republicanTieVotes:
        democraticDistricts += 1
    else:
        republicanDistricts += 1

    totalRepublicanVotes += republicanTieVotes
    totalDemocratVotes += democratTieVotes
    
    print("Total Republican Votes = ", totalRepublicanVotes)
    print("Total Democratic Votes = ", totalDemocratVotes)
    print("Republican Districts Won = ", republicanDistricts)
    print("Democratic Districts Won = ", democraticDistricts)
    if republicanDistricts > democraticDistricts:
        print("Republicans win the election.")
    else:
        print("Democrats win the election.") 
    print()
    if democraticDistricts > republicanDistricts:
        totalDemocratWins += 1
    else:
        totalRepublicanWins += 1
    elections += 1
print("Gerrymandering simulation results for",districts,"districts with",districtVoters,"voters each:")
print("Total number of election simulations = ", totalElectionTrials)
print("Total Democratic Wins = ", totalDemocratWins)
print("Total Republican Wins = ", totalRepublicanWins)



