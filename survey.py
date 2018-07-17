import json
import os


questions = ["What's your name? \n", "How old are you? \n", "What school do you go to? \n", "Favorite school subject? \n"]

cont = True
data = []
while cont:
    answers = {}
    for q in questions:
        answers[q] = input(q)
    data.append(answers)
    contin =(input("Would you like to continue? Y/N "))
    if contin == "Y":
        cont = True
    else:
        cont = False

if os.path.isfile("data.json"):
    file = open("data.json", "r+")
    old_data = json.load(file)
    old_data.extend(data)
    file.write(json.dumps(old_data))
    file.close()
else:
    file = open("data.json", "w") #create a file called data.json, with the write permission
    file.write(json.dumps(data)) #write json object to our file
    file.close()
