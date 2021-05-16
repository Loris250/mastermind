import random

### variables ###

colors: list = ["blue", "green", "yellow", "red", "orange", "pink"] # colors to be used in game

code: list = [] # list containing random arrangement of 4 colors to be found out be user

response: list = [] # list containing black or white as response to user_list

user_list: list = [] # liste contenant la liste de couleur entrée par l'utilisateur 

verification = 0 #argument 0 = faux et 1 = vrai pour savoir si l'entrée par l'utilisateur est valideé 

gameWon: bool = False # boolean to know if the user has found the code

### fonctions ###

def getList():
    input_string: str = input("Enter a code of four colors (blue, green, yellow, red, orange or pink) separated by a space: ")
    user_list: list = input_string.split()
    return user_list

    ### code ###

def generercode(): 
    for i in range(4): # generating random code
        code.append(random.choice(colors))
    print("Le code est: ", code)
    return code 

### début du programme ### 

code = generercode() # on commence par générer un code: une séquence de 4 couleurs 

print(len(code))



###étape de vérification de l'entrée du code###

while len(code) != len(user_list):         
    user_list = getList()                   # ask user to enter a code
    print("La liste de couleur entrée par l'utilisateur est: ", user_list)
    print(len(user_list))
    a = 1
    for i in range(4): 
        if user_list[i] not in colors: 
            print("Entrez une liste avec les couleurs qui sont données")
            a = 2
            break 

    if not len(code) == len(user_list):
        print("Enter a code of length 4 !!!!") 
        verification = 0    
        a = 2

    if a == 1: 
        print("Le format de la liste entrée par l'utilisateur est validé ")
        verification = 1 # on peut maintenant commencer à comparer les listes



    if a == 2: 
        print("Le format de la liste entrée par l'utilisateur n'est pas validé, veuillez entrer une nouvelle liste")
        user_list = []
    #######



while gameWon == False and verification ==  1:

    code_copy = code

    if code == user_list:
        response = 4*["black"]
        print("Congrats,you have found the code!")
        gameWon = True
        break

    # compare exact positions
    for i in range(4):
        if code_copy[i] == user_list[i]:
            response.append("black")
            code_copy[i] = "0"
            user_list[i] = "rien"

    print(code_copy)
    print(response)


    #comparer les couleurs 

    for i in range(4):
         for n in range(4):
             if user_list[i] == code_copy[n]:
                response.append("white")
                user_list[i] = "rien"
                code_copy[n] = "0"
    print(code_copy)
    print(response)

    break
