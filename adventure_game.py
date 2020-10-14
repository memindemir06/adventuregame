# --- My Test Based Adventure Game ---
import time, os

print("Loading...")

time.sleep(2)

print("Welcome to my game! " + os.getlogin() + "\nPlease choose a character from the list:")

characterList = ["Knight", "Warrior", "Wizard"]

i = 1
for x in characterList:
	print(str(i) + ". " + x)
	i+=1

character = int(input("Type in your character number: "))

while character not in range(1,i):
	print("Please type in a valid number.")
	character = int(input("Type in your character number: "))
else:
	selectedCharacter = characterList[character -1]
	print("You chose: " + selectedCharacter)
	