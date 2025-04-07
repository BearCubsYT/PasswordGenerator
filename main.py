import random

# All Data List
all_data = []

def cleanData(data: str):
    data = data.strip().lower().replace(" ", "")
    return data

def getPassSec1():
    print("What is your favorite color?")
    current_response = input("")
    cleaned_response = cleanData(current_response)
    all_data.append(cleaned_response)

def getPassSec2():
    getPassSec1()
    # Question 2
    print("Do you like dogs?")
    current_response = input("")
    cleaned_response = cleanData(current_response)
    if cleaned_response == "yes":
        random_num = random.randint(1,3)
        if random_num == 1:
            all_data.append("lover")
        elif random_num == 2:
            all_data.append("finder")
        else:
            all_data.append("hater")
    else:
        random_num = random.randint(1,3)
        if random_num == 1:
            all_data.append("stealer")
        elif random_num == 2:
            all_data.append("puncher")
        else:
            all_data.append("kicker")

def getPassSec3():
    getPassSec2()
    # Question 3
    print("What is your favorite number?")
    current_response = input("")
    cleaned_response = cleanData(current_response)
    all_data.append(cleaned_response)

def randomizeData():
    getPassSec3()
    final_string = ""
    for sec in all_data:
        times = 0
        for char in sec:
            random_num = random.randint(1,2)
            if random_num == 1 and char != "0" and char != "1" and char != "2" and char != "3" and char != "4" and char != "5" and char != "6" and char != "7" and char != "8" and char != "9":
                char = char.capitalize()
                final_string = final_string + char
            else:
                final_string = final_string + char

            times += 1
    
    print(f"Your Password: {final_string}")

randomizeData()