# --- My Test Based Adventure Game ---
print("Welcome to my game!")

playerName = input("What is your name? ")

print("Hello " + playerName)

print("Choose a character:", "1. Knight", "2. Warrior", "3. Wizard", sep='\n')

characterList = ["Knight", "warrior", "Wizard"]

character = input("Type in your character number: ")

print("You chose: " + characterList[int(character) -1])
