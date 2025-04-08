import random
import json
import colorama as ca
import time
ca.init(autoreset=True)

active = True
UNDERLINE = '\033[4m'
RESET = '\033[0m'

def PrintLogo():
    print(ca.Fore.RED + ca.Style.BRIGHT + "\n\n    .===========.")
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
    print(ca.Fore.GREEN + "  Show Website (Web=)")
    print(ca.Fore.GREEN + "  Show Accounts (Accs=)")

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
        else:
            found = False
    if not found:
        with open("passwords.json", "w") as f:
                json.dump(data, f, indent=4)
        

while active:
    PrintLogo()
    PrintChoices()
    choice = input(f"{ca.Fore.CYAN}{UNDERLINE}")
    if choice.lower().replace(" ", "") == "web+":
        NewWeb()

    

# # All Data List
# all_data = []

# def cleanData(data: str):
#     data = data.strip().lower().replace(" ", "")
#     return data

# def getPassSec1():
#     print("What is your favorite color?")
#     current_response = input("")
#     cleaned_response = cleanData(current_response)
#     all_data.append(cleaned_response)

# def getPassSec2():
#     getPassSec1()
#     # Question 2
#     print("Do you like dogs?")
#     current_response = input("")
#     cleaned_response = cleanData(current_response)
#     if cleaned_response == "yes":
#         random_num = random.randint(1,3)
#         if random_num == 1:
#             all_data.append("lover")
#         elif random_num == 2:
#             all_data.append("finder")
#         else:
#             all_data.append("hater")
#     else:
#         random_num = random.randint(1,3)
#         if random_num == 1:
#             all_data.append("stealer")
#         elif random_num == 2:
#             all_data.append("puncher")
#         else:
#             all_data.append("kicker")

# def getPassSec3():
#     getPassSec2()
#     # Question 3
#     print("What is your favorite number?")
#     current_response = input("")
#     cleaned_response = cleanData(current_response)
#     all_data.append(cleaned_response)

# def randomizeData():
#     getPassSec3()
#     final_string = ""
#     for sec in all_data:
#         times = 0
#         for char in sec:
#             random_num = random.randint(1,2)
#             if random_num == 1 and char != "0" and char != "1" and char != "2" and char != "3" and char != "4" and char != "5" and char != "6" and char != "7" and char != "8" and char != "9":
#                 char = char.capitalize()
#                 final_string = final_string + char
#             else:
#                 final_string = final_string + char

#             times += 1
    
#     print(f"Your Password: {final_string}")

# randomizeData()

titleScreen()