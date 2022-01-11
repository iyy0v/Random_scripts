import random
import time

def menu(computerScore,userScore):
	print("\n\n =================================================")
	print("\t User : " + str(userScore) + "\t\t Computer : " + str(computerScore))
	print(" -------------------------------------------------")
	print("\n What is your play :\n")
	print("\n \t[1] Rock")
	print("\n \t[2] Paper")
	print("\n \t[3] Scissors")
	print("\n\n \t[0] Exit")

def checkResult(cPlay,uPlay):
	global computerScore,userScore
	plays = ["Rock","Paper","Scissors"]

	print(" -------------------------------------------------")
	print("\n You played : " + plays[uPlay-1] + "\t\t Computer played : " + plays[cPlay-1])
	if(cPlay == uPlay):
		print("\n \t\t Result : Draw")
	elif((cPlay == 1 and uPlay == 2) or (cPlay == 2 and uPlay == 3) or (cPlay == 3 and uPlay == 1)):
		print("\n \t\t Result : You won !")
		userScore += 1
	else:
		print("\n \t\t Result : Computer won !")
		computerScore += 1

run = 1
computerScore = 0
userScore = 0

while(run):
	menu(computerScore,userScore)
	userPlay = int(input())
	if(userPlay < 0 or userPlay > 3):
		print("\n Unknown play ! please choose again.")
	elif(userPlay == 0):
		print("\n Thanks for playing !")
		run = 0
	else:
		computerPlay = random.randint(1,3)
		checkResult(computerPlay,userPlay)
		time.sleep(2)