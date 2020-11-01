# --- My Test Based Adventure Game ---
import time, os

print("Loading...")

time.sleep(0.75)

playerSettings = list()
with open("settings.txt") as file:
	playerSettings = file.readlines()

playerSettings = [line.rstrip('\n') for line in open("settings.txt")]

if playerSettings[0] == "Default":
	playerSettings[0] = os.getlogin()
	with open("settings.txt", "w") as file:
		for item in playerSettings:
			file.write("%s\n" % item)

characterList = ["Knight", "Warrior", "Wizard"]

if playerSettings[1] == "Default":
	print("Welcome to my game! " + playerSettings[0] + "\nPlease choose a character from the list:")
	for idx, val in enumerate(characterList, start = 1):
		print(" " + str(idx) + ". " +val)

	character = int(input("Type in your character number: "))

	while character not in range(1,idx+1):
		print("Please type in a valid number.")
		character = int(input("Type in your character number: "))
	else:
		playerSettings[1] = characterList[character -1]
		print("\nHey " + playerSettings[1] + "!")
else:
	print("Welcome back, %s the %s" %(playerSettings[0],playerSettings[1]))

while True:
	menu = int(input("\nWould you like to start the adventure (1), change settings? (2), view settings (3), save game and quit (4), or reset settings(5)?\n"))
	if (menu == 1):

		move = input("\n" + playerSettings[1] + ", do u want to move?\n")
		count = 0
		while move in ('Yes', 'yes', 'YES', 'y', 'Y'):
			print("You moved forwards 1 step")
			move = input("Keep moving?\n")
			count += 1
		else:
			print("You moved " + str(count) + " spaces.")
			playerSettings[3] = int(playerSettings[3]) + count
			with open("settings.txt", "w") as file:
				for item in playerSettings:
					file.write("%s\n" % item)
			break


	elif (menu == 2):
		print("1. Name: %s \n2. Character Name: %s \n3. Character Age: %s" %(playerSettings[0],playerSettings[1],playerSettings[2]))
		settingChange = int(input("What do u want to change? \n"))
		if settingChange == 2:
			for idx, val in enumerate(characterList, start = 1):
				print(" " + str(idx) + ". " +val)

			character = int(input("Type in your new character number: "))
			playerSettings[settingChange -1] = characterList[character -1]
			print("You are now a " + playerSettings[1])
		else:
			newValue = input("What is the new input?\n")
			playerSettings[settingChange - 1] = newValue
	elif (menu == 3):
		print("Name: %s \nCharacter Name: %s \nCharacter Age: %s" %(playerSettings[0],playerSettings[1],playerSettings[2]))
	elif (menu == 4):
		with open("settings.txt", "w") as file:
			for item in playerSettings:
				file.write("%s\n" % item)
			time.sleep(0.5)
			print("Game saved...")
			break
	elif (menu == 5):
		print("Warning! This will delete all your progress and current settings, and you will quit the game.\n")
		choice = input("Are you sure? (y) or (n): ")
		if choice == "y":
			playerSettings = ["Default","Default","0","0"]
			with open("settings.txt", "w") as file:
				for item in playerSettings:
					file.write("%s\n" % item)
			break
		else:
			continue
	else:
		print("Please type in a valid number (1,2,3,4 or 5)")