# --- My Test Based Adventure Game ---
import time, os

print("Loading...")

time.sleep(2)

playerSettings = {
	"name": os.getlogin(),
	"characterName": "",
	"characterAge": "520"
}

print("Welcome to my game! " + playerSettings.get("name") + "\nPlease choose a character from the list:")

characterList = ["Knight", "Warrior", "Wizard"]

#i = 1
#for x in characterList:
#	print(str(i) + ". " + x)
#	i+=1

for idx, val in enumerate(characterList, start = 1):
	print(" " + str(idx) + ". " +val)

character = int(input("Type in your character number: "))

while character not in range(1,idx+1):
	print("Please type in a valid number.")
	character = int(input("Type in your character number: "))
else:
	playerSettings["characterName"] = characterList[character -1]
	print("You chose: " + playerSettings.get("characterName"))

settingMenu = ['PlayerName', 'CharacterName', 'CharacterAge', 'View Current Settings']

while True:
	menu = (input("\nWould you like to start the adventure or change settings?\n"))
	if (int(menu) == 1):
		move = input("\n" + playerSettings["characterName"] + ", do u want to move?\n")
		count = 0
		while move in ('Yes', 'yes', 'YES', 'y', 'Y'):
			print("You moved forwards 1 step")
			move = input("Keep moving?\n")
			count += 1
		else:
			print("U moved " + str(count) + " spaces.")
			break
	elif (int(menu) == 2):
		for idx, val in enumerate(settingMenu, start = 1):
			print(" " + str(idx) + ". " +val)

		settingChange = int(input("What do u want to change? \n"))

		if (settingChange == 1):
			playerSettings["name"] = input("Please enter a new name: ")
			print("Player name is now " + playerSettings["name"] + ".")
		elif settingChange == 2:
			for idx, val in enumerate(characterList, start = 1):
				print(" " + str(idx) + ". " +val)

			character = int(input("Type in your character number: "))
			playerSettings["characterName"] = characterList[character -1]
			print("Character name is now " + playerSettings["characterName"] + ".")
		elif settingChange == 3:
			playerSettings["characterAge"] = input("Please enter ur age: ")
			print("Player age is now " + playerSettings["characterAge"] + ".")
		elif settingChange == 4:
			print(playerSettings)
	else:
		print("Please type in a valid number (1 or 2)")