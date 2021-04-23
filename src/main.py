import random

### variables ###

colors: list = ["blue", "green", "yellow", "red", "orange", "grey"] # colors to be used in game

code: list = [] # list containing random arrangement of 4 colors to be found out be user

response: list = [] # list containing black or white as response to user_list

gameWon: bool = False # boolean to know if the user has found the code

### functions ###

def getList():
    input_string: str = input("Enter a code of four colors (blue, green, yellow, red, orange or grey) separated by a space: ")
    user_list: list = input_string.split()
    return user_list

### code ###


for i in range(4): # generating random code
    code.append(random.choice(colors))


code_copy = code
print(code)

user_list = []

while len(code) != len(user_list):         
    user_list = getList()                   # ask user to enter a code
    print(user_list)
    if len(code) != len(user_list):
        print("Enter a code of length 4 !!!!")   # verification for uncapable users :)


while gameWon == False:
    
    # compare whole list

    if code == user_list:
        response = 4*["black"]
        print("Congrats,you have found the code!")
        gameWon = True
        break

    # compare exact positions
    for i in range(4):
        if code_copy[i] == user_list[i]:
            response = response + ["black"]
            code_copy[i] = "0"


    # compare colors
    for i in range(4):
         for n in range(4):
             if user_list[i]== code_copy[n]:
                 response = response + ["white"]
                 code_copy[i] = "0"

    print(response)

    getList()