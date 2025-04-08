import random
import json
import colorama as ca
import time
ca.init(autoreset=True)

userNameWords1 = ["Cute", "Funny", "Chill", "Smart", "Lazy", "Happy", "Sneaky", "Witty", "Bold", "Shy",
"Lucky", "Weird", "Cool", "Spooky", "Zany", "Tiny", "Brave", "Grumpy", "Jolly", "Funky",
"Bright", "Clever", "Nerdy", "Moody", "Bouncy", "Quirky", "Gloomy", "Snappy", "Swift", "Curious",
"Goofy", "Quiet", "Loud", "Icy", "Warm", "Crispy", "Edgy", "Sleepy", "Feisty", "Crafty",
"Cheeky", "Bossy", "Silly", "Vain", "Greedy", "Snug", "Yummy", "Spicy", "Zesty", "Spunky",
"Noisy", "Nimble", "Wobbly", "Rusty", "Lush", "Dusty", "Misty", "Cranky", "Tough", "Snarky",
"Frisky", "Sniffy", "Giddy", "Snazzy", "Perky", "Gritty", "Zappy", "Stormy", "Snoozy", "Dreamy",
"Peppy", "Dopey", "Nutty", "Tasty", "Rowdy", "Nifty", "Fizzy", "Sketchy", "Whiny", "Greasy",
"Sassy", "Dizzy", "Fluffy", "Crisp", "Chubby", "Plucky", "Jumpy", "Speedy", "Slinky", "Wavy",
"Cheesy", "Frosty", "Toasty", "Cloudy", "Flaky", "Grimy", "Jazzy", "Rustic", "Zippy", "Quaint"]

usernameWords2 = ["Panda", "Banana", "Goblin", "Fox", "Potato", "Ghost", "Waffle", "Noodle", "Sloth", "Bean",
"Dragon", "Kitten", "Wizard", "Pumpkin", "Gnome", "Penguin", "Unicorn", "Muffin", "Taco", "Bunny",
"Zombie", "Duck", "Cupcake", "Dino", "Hamster", "Robot", "Bear", "Tiger", "Pigeon", "Cactus",
"Otter", "Snail", "Sheep", "Moose", "Donut", "Octopus", "Llama", "Crab", "Raccoon", "Socks",
"Ferret", "Pickle", "Tofu", "Yeti", "Lizard", "Peach", "Narwhal", "Toad", "Frog", "Churro",
"Giraffe", "Meerkat", "Seagull", "Bubble", "Sushi", "Koala", "Beetle", "Cookie", "Marshmallow", "Pizza",
"Penguin", "Chinchilla", "Shrimp", "Flamingo", "Snickers", "Turtle", "Fungus", "Cheesecake", "Kiwi", "Pretzel",
"Whale", "Bacon", "Crouton", "Lemon", "Mango", "Sprout", "Peanut", "Skunk", "Raisin", "Turnip",
"Walrus", "Omelette", "Tangerine", "Bagel", "Nugget", "Parrot", "Trombone", "Sock", "Stump", "Icicle",
"Fritter", "Acorn", "Broccoli", "Spinach", "Worm", "Popcorn", "Pickaxe", "Mushroom", "Twig", "Clam"]

passswordChars = [
  "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
  "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
  "0","1","2","3","4","5","6","7","8","9",
  "!","\"","#","$","%","&","'","(",")","*","+",
  ",","-",".","/",":",";","<","=",">","?","@",
  "[","\\","]","^","_","`","{","|","}","~"
]


active = True
UNDERLINE = '\033[4m'
RESET = '\033[0m'

def PrintLogo():
    print(RESET + ca.Fore.RED + ca.Style.BRIGHT + "\n\n    .===========.")
    print(ca.Fore.RED + ca.Style.BRIGHT + "    |           |") 
    print(ca.Fore.RED + ca.Style.BRIGHT + "    |password   |")  
    print(ca.Fore.RED + ca.Style.BRIGHT + "    |    manager|")
    print(ca.Fore.RED + ca.Style.BRIGHT + "    |___________|")
    print(ca.Fore.RED + ca.Style.BRIGHT + "    |_________-_|_,-.")
    print(ca.Fore.RED + ca.Style.BRIGHT + "    [_____________]   )")
    print(ca.Fore.RED + ca.Style.BRIGHT + "    .,,,,,,,,,, ,,.  (_")
    print(ca.Fore.RED + ca.Style.BRIGHT + "    /,,,,,,,,,,, ,,,\\ (>\\") 
    print(ca.Fore.RED + ca.Style.BRIGHT + "    (______.-``-._____) \\__)\n")

def PrintChoices():
    print(RESET + ca.Fore.GREEN + ca.Style.BRIGHT + "Choices: ")
    print(ca.Fore.GREEN + "  New Website (Web+)")
    print(ca.Fore.GREEN + "  New Account (Acc+)")
    print(ca.Fore.GREEN + "  Delete Website (Web-)")
    print(ca.Fore.GREEN + "  Delete Account (Acc-)")
    print(ca.Fore.GREEN + "  Show Websites (Web=)")
    print(ca.Fore.GREEN + "  Show Accounts (Acc=)")

def NewWeb():
    with open("Code/passwords.json") as f:
        data = json.load(f)
    print(RESET + ca.Fore.GREEN + "\n\nEnter Website Name:")
    websiteName = input(f"{ca.Fore.CYAN}{UNDERLINE}  ")
    for website in data:
        if website == websiteName:
            print(RESET + ca.Fore.RED + "\nSorry, you already added this website, try again!")
            time.sleep(1)
            found = True
            break
        else:
            found = False
    if not found:
        data[websiteName] = {}
        print(RESET+ ca.Fore.YELLOW + f"Website succesfully added")
        with open("Code/passwords.json", "w") as f:
                json.dump(data, f, indent=4)

def AccCreate(website: str):
    print(RESET + ca.Fore.GREEN + "\n\nWould you like to generate a username? (yes/no)")
    generatePick = input(f"{ca.Fore.CYAN}{UNDERLINE}  ")
    if generatePick.lower().replace(" ", "") == "yes":
        userPart1 = userNameWords1[random.randint(1,100)]
        userPart2 = usernameWords2[random.randint(1,100)]
        userNum = random.randint(1,100)
        userName = f"{userPart1}{userPart2}{userNum}"
        print(RESET + f"Your generated username is {userName}")
    else:
        print(RESET + ca.Fore.GREEN + "\n\nPlease enter your chosen username:")
        userName = input(f"{ca.Fore.CYAN}{UNDERLINE}  ")

    print(RESET + ca.Fore.GREEN + "\n\nWould you like to generate a password? (yes/no)")
    generatePick = input(f"{ca.Fore.CYAN}{UNDERLINE}  ")
    if generatePick.lower().replace(" ", "") == "yes":
        password = ""
        for x in range(13):
            password = password + passswordChars[random.randint(0,93)]
        print(RESET + f"Your generated password is {password}")
    else:
        print(RESET + ca.Fore.GREEN + "\n\nPlease enter your chosen password:")
        password = input(f"{ca.Fore.CYAN}{UNDERLINE}  ")
    
    print(RESET + f"Username: {userName}")
    print(f"Password: {password}")

    print(RESET+ ca.Fore.YELLOW + f"Account succesfully created")
    return userName, password

def NewAcc():
    with open("Code/passwords.json") as f:
        data = json.load(f)
    
    print(RESET + ca.Fore.GREEN + "\n\nWhich website would you like an account for?\n")
    print(ca.Fore.BLUE + "Websites:")
    for website in data:
        print(ca.Fore.GREEN + website)
    
    websitePick = input(f"\n{ca.Fore.CYAN}{UNDERLINE}  ")
    for website in data:
        if website == websitePick:
            found = True
            break
        else:
            found = False
    if found:
        theData = AccCreate(websitePick)
        data[websitePick][theData[0]] = {
            "password": theData[1]
        }
        with open("Code/passwords.json", "w") as f:
                json.dump(data, f, indent=4)
    else:
        print(RESET + ca.Fore.RED + "\nSorry, you don't have that website, try adding it in the Website Creation page!")
    
def DelWeb():
    with open("Code/passwords.json") as f:
        data = json.load(f)
    
    print(RESET + ca.Fore.GREEN + "\n\nWhich website would you like to delete?\n")
    print(ca.Fore.BLUE + "Websites:")
    for website in data:
        print(ca.Fore.GREEN + website)
    
    websitePick = input(f"\n{ca.Fore.CYAN}{UNDERLINE}  ")

    found = False
    for website in data:
        if website == websitePick:
            found = True
            break
    
    if found:
        del data[website]
        print(RESET+ ca.Fore.YELLOW + f"Website succesfully deleted")
    else:
        print(RESET + ca.Fore.RED + "Sorry, we couldn't find that website")
    
    with open("Code/passwords.json", "w") as f:
        json.dump(data, f, indent=4)

def DelAcc():
    with open("Code/passwords.json") as f:
        data = json.load(f)
    
    print(RESET + ca.Fore.GREEN + "\n\nWhich website would you like to delete an account for?\n")
    print(ca.Fore.BLUE + "Websites:")
    for website in data:
        print(ca.Fore.GREEN + website)
    
    websitePick = input(f"\n{ca.Fore.CYAN}{UNDERLINE}  ")

    found = False
    for website in data:
        if website == websitePick:
            found = True
            break
    
    if found:
        print(RESET + ca.Fore.GREEN + "\n\nWhich account would you like to delete?\n")
        print(ca.Fore.BLUE + f"{websitePick}:")
        for account in data[websitePick]:
            print(ca.Fore.GREEN + account)
        
        accountPick = input(f"\n{ca.Fore.CYAN}{UNDERLINE}  ")

        found = False
        for account in data[websitePick]:
            if account == accountPick:
                found = True
                break
        
        if found:
            del data[websitePick][accountPick]
            print(RESET+ ca.Fore.YELLOW + f"Account succesfully deleted")
        else:
            print(RESET + ca.Fore.RED + "Sorry, we couldn't find that account")
        
        with open("Code/passwords.json", "w") as f:
            json.dump(data, f, indent=4)

def AllWeb():
    with open("Code/passwords.json") as f:
        data = json.load(f)
    print(ca.Fore.BLUE + "\n\nWebsites:")
    for website in data:
        print(ca.Fore.GREEN + website)
    
    print("Press enter when done")
    input()

def AllAcc():
    with open("Code/passwords.json") as f:
        data = json.load(f)
    print("\n\n")
    for website in data:
        print(RESET + ca.Fore.GREEN + f"{website}:")
        for account in data[website]:
            print(ca.Fore.GREEN + f"  {account}: {data[website][account]["password"]}")
    
    print("Press enter when done")
    input()

while active:
    PrintLogo()
    PrintChoices()
    choice = input(f"{ca.Fore.CYAN}{UNDERLINE}")
    if choice.lower().replace(" ", "") == "web+":
        NewWeb()
    elif choice.lower().replace(" ", "") == "acc+":
        NewAcc()
    elif choice.lower().replace(" ", "") == "web-":
        DelWeb() 
    elif choice.lower().replace(" ", "") == "acc-":
        DelAcc() 
    elif choice.lower().replace(" ", "") == "web=":
        AllWeb() 
    elif choice.lower().replace(" ", "") == "acc=":
        AllAcc() 