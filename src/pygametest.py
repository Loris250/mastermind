#########################################################################
#              Importations des modules
##########################################################################



import pygame #module pygame 
import sys #module nécessaire pour bien fermer le programme
import random #module random nécessaire pour générer un code 

#################################################################################
#importation du code précédent pour générer une séquence ainsi que vérifier et donner les résultats.
################################################################################################


colors: list = ["blue", "green", "yellow", "red", "orange", "pink"] # colors to be used in game

code: list = [] # list containing random arrangement of 4 colors to be found out be user

response: list = [] # list containing black or white as response to user_list

user_list: list = [] # liste contenant la liste de couleur entrée par l'utilisateur 

def generercode(): 
    for i in range(4): # generating random code
        code.append(random.choice(colors))
    return code 

code = generercode() #on genere un code 
print(code)

########################################
#verification du code
##############################################

def verificationcode(solution, codeutilisateur):
    
    code_copy = solution
    response = []

    if solution == codeutilisateur:
        response = 4*["black"]

    else: 
        for i in range(4):
            if code_copy[i] == codeutilisateur[i]:
                response.append("black")
                code_copy[i] = "0"
                codeutilisateur[i] = "rien"


        for i in range(4):
            for n in range(4):
                 if codeutilisateur[i] == code_copy[n]:
                    response.append("white")
                    codeutilisateur[i] = "rien"
                    code_copy[n] = "0"
    
    return response






############################################################################
#               Initialisation du jeu pygame
###########################################################################



pygame.init() #initialisation du module pygame (indispensable)

screen = pygame.display.set_mode((1000,1000)) #definition de la taille de la fenêtre (ex: 400x500) #c'est une surface primaire, le display surface est unique
timer = pygame.time.Clock() #definitiion de la fonction qui définit le nombre d'image par seconde (raffraichissement du jeu)


#################################################################################################################
#################################################################################################################



banniere =pygame.Rect(0,0,1000,200) #definition d'une surface ou l'on affichera du texte ou le titre

###########################################################################################################
#definition des cases: 


#definition de la position de cases
ligne1 = {
    'Aa': pygame.Rect(250,250,50,50),
    'Ab': pygame.Rect(350,250,50,50),
    'Ac': pygame.Rect(450,250,50,50),
    'Ad': pygame.Rect(550,250,50,50),
}

#definition des couleurs des cases, l'utilisation des dictionnaires est très importante 
couleur = {
    "Aa": "blue", 
    "Ab": "blue",
    "Ac": "blue", 
    "Ad": "blue", 
    
}

############################################################################################
#definition des cases de réponses
###########################################################################################

repcase1 = {
    "i": pygame.Rect(700,250,50,50),
    "ii": pygame.Rect(750,250,50,50),
    "iii": pygame.Rect(800,250,50,50),
    "iv": pygame.Rect(850,250,50,50),
}

repcase1couleur = {
    "i": "white",
    "ii": "white",
    "iii": "white",
    "iv": "black",

}






#Position de base du pointer

x = 250
y = 250

##################################################################################
#les verifications des lignes sont éteintes de base
##################################################################################
verifyline1 = False
verifyline2 = False
verifyline3 = False
verifyline4 = False
#etc





game_on = True #variable qui définit que le jeu est allumé


while game_on == True:

    pointer = pygame.Rect(x,y,50,50)
    for event in pygame.event.get():  #Pour chaque élément qu'il se passe lors du fonctionnement du jeu pygame: 
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() #permet de quitter le programme quand on appuie sur la croix rouge, le sys exit est nécessaire pour que le programme s'arrête complètement


    screen.fill(pygame.Color("white")) #on veut un display screen de couleur blanche


    pygame.draw.rect(screen, pygame.Color("red"), banniere) #on dessine la bannière


    pygame.draw.rect(screen, pygame.Color(couleur["Aa"]), ligne1["Aa"])
    pygame.draw.rect(screen, pygame.Color(couleur["Ab"]), ligne1["Ab"])
    pygame.draw.rect(screen, pygame.Color(couleur["Ac"]), ligne1["Ac"])
    pygame.draw.rect(screen, pygame.Color(couleur["Ad"]), ligne1["Ad"])

    pygame.draw.rect(screen, pygame.Color("black"), pointer, 3)



#Pour obtenir les données du clavier:
    keys = pygame.key.get_pressed()


#Pour faire bouger le pointer de gauche à droite: 
    if keys[pygame.K_LEFT] and x>250:
        x = x - 100
    if keys[pygame.K_RIGHT] and x<550:
        x = x + 100


#Pour connaître la case sélectionnée par le pointer
    for i in ligne1:
        if ligne1[i] == pygame.Rect(x,y,50,50):
            selection = i


    ####################################################################################
    #Changements de couleur avec les touches
    #####################################################################################
    if keys[pygame.K_b]:
        couleur[selection] = "blue"

    if keys[pygame.K_g]: 
        couleur[selection] = "green"

    if keys[pygame.K_y]:
        couleur[selection] = "yellow"

    if keys[pygame.K_r]: 
        couleur[selection] = "red"

    if keys[pygame.K_o]:
        couleur[selection] = "orange"

    if keys[pygame.K_p]:
        couleur[selection] = "pink"


###################################################################################
#décodage de la séquence de la ligne 1: 
###################################################################################

        
    reponseligne1 = []
    for i in couleur: 
        reponseligne1.append(couleur[i])
    
    ############################################
    ##########################################

#clavier pour vérifier les lignes:
    if keys[pygame.K_1]:
        verifyline1 = True
    if keys[pygame.K_2]:
        verifyline2 = True
    if keys[pygame.K_3]:
        verifyline3 = True
    if keys[pygame.K_4]:
        verifyline4 = True




    #donner la vérification de la ligne 1: 
    if verifyline1 == True:

        resultligne1 = verificationcode(code,reponseligne1)
        print(resultligne1, "o")
        print(reponseligne1)
        print(code, "ee")


        pygame.draw.rect(screen, pygame.Color(repcase1couleur["i"]), repcase1["i"])
        pygame.draw.rect(screen, pygame.Color(repcase1couleur["ii"]), repcase1["ii"])
        pygame.draw.rect(screen, pygame.Color(repcase1couleur["iii"]), repcase1["iii"])
        pygame.draw.rect(screen, pygame.Color(repcase1couleur["iv"]), repcase1["iv"])





#rafraichissement de la page, puis timer afin que tout fonctionne bien avec les transitions
    pygame.display.update()
    timer.tick(10) #définition du timer à 60 images par secondes 



