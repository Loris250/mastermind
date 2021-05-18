#########################################################################
#              Importations des modules
##########################################################################



import pygame #module pygame 
import sys #module nécessaire pour bien fermer le programme
import random #module random nécessaire pour générer un code 

#################################################################################
#importation du code précédent pour générer une séquence ainsi que vérifier et donner les résultats.
################################################################################################

#Liste des couleurs disponibles pour la génération d'une séquence "code à deviner":

colors: list = ["blue", "green", "yellow", "red", "orange", "pink"] 

#Definition de la liste qui va contenir le code: 

code: list = [] 

#Definition de la liste qui contient la séquence de couleur entrée par l'utilisateur

user_list: list = [] 

#Definition de la liste qui contient les valeurs  de vérifications donnée par la fonction de vérification. (contient white ou black): 

response: list = [] 

#Fonction qui génère la séquence "code"

def generercode(): 
    for i in range(4): # generating random code
        code.append(random.choice(colors))
    return code 
    
code = generercode() #on genere un code 

print("Le code est: ", code)



########################################
#Fonction qui vérifie la séquence entrée par l'utilisateur,   
##############################################

def verificationcode(solution, essai):
    
    copy_solution = solution.copy() #Problème réglé !! problème: les variables pointent vers les mm emplacements dans la mémoire
    response = []

    if solution == essai:
        response = 4*["black"]

    else: 
        for i in range(4):
            if copy_solution[i] == essai[i]:
                response.append("black")
                copy_solution[i] = "0"
                essai[i] = "rien"


        for i in range(4):
            for n in range(4):
                 if essai[i] == copy_solution[n]:
                    response.append("white")
                    essai[i] = "rien"
                    copy_solution[n] = "0"
    
    return response






############################################################################
#               Initialisation du jeu pygame
###########################################################################



pygame.init() #initialisation du module pygame (indispensable)

screen = pygame.display.set_mode((1100,1000)) #definition de la taille de la fenêtre (ex: 400x500) #c'est une surface primaire, le display surface est unique
timer = pygame.time.Clock() #definitiion de la fonction qui définit le nombre d'image par seconde (raffraichissement du jeu)


#################################################################################################################
#################################################################################################################



banniere =pygame.Rect(0,0,1100,200) #definition d'une surface ou l'on affichera du texte ou le titre

###########################################################################################################
#definition des cases: 


#definition de la position de cases

#ligne1: 
ligne1 = {
    'Aa': pygame.Rect(250,250,50,50),
    'Ab': pygame.Rect(350,250,50,50),
    'Ac': pygame.Rect(450,250,50,50),
    'Ad': pygame.Rect(550,250,50,50),
}

#ligne2: 
ligne2 = {
    'Ba': pygame.Rect(250,350,50,50),
    'Bb': pygame.Rect(350,350,50,50),
    'Bc': pygame.Rect(450,350,50,50),
    'Bd': pygame.Rect(550,350,50,50),
}
#ligne3: 
ligne3 = {
    'Ca': pygame.Rect(250,450,50,50),
    'Cb': pygame.Rect(350,450,50,50),
    'Cc': pygame.Rect(450,450,50,50),
    'Cd': pygame.Rect(550,450,50,50),
}
#ligne4: 
ligne4 = {
    'Da': pygame.Rect(250,550,50,50),
    'Db': pygame.Rect(350,550,50,50),
    'Dc': pygame.Rect(450,550,50,50),
    'Dd': pygame.Rect(550,550,50,50),
}


#definition des couleurs des cases, l'utilisation des dictionnaires est très importante 
couleur = {
    "Aa": "blue", 
    "Ab": "blue",
    "Ac": "blue", 
    "Ad": "blue", 
    #deuxième ligne
    "Ba": "blue",
    "Bb": "blue", 
    "Bc": "blue",
    "Bd": "blue", 
    #3ième ligne 
    "Ca": "blue",
    "Cb": "blue", 
    "Cc": "blue",
    "Cd": "blue", 
    #4ième ligne 
    "Da": "blue",
    "Db": "blue", 
    "Dc": "blue",
    "Dd": "blue", 


    
}



############################################################################################
#definition des cases de réponses
###########################################################################################

repcase1 = {
    0: pygame.Rect(700,250,50,50),
    1: pygame.Rect(800,250,50,50),
    2: pygame.Rect(900,250,50,50),
    3: pygame.Rect(1000,250,50,50),
}

repcase1couleur = {
    0: "white",
    1: "white",
    2: "white",
    3: "black",

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

affichagel1 = False
affichagel2 = False
affichagel3 = False
affichagel4 = False

resultline1 = []
resultline2 = []
resultline3 = []
resultline4 = []
#etc





game_on = True #variable qui définit que le jeu est allumé


while game_on == True:

    pointer = pygame.Rect(x,y,50,50)
    for event in pygame.event.get():  #Pour chaque élément qu'il se passe lors du fonctionnement du jeu pygame: 
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() #permet de quitter le programme quand on appuie sur la croix rouge, le sys exit est nécessaire pour que le programme s'arrête complètement


    screen.fill(pygame.Color("grey")) #on veut un display screen de couleur blanche


    pygame.draw.rect(screen, pygame.Color("red"), banniere) #on dessine la bannière



    pygame.draw.rect(screen, pygame.Color(couleur["Aa"]), ligne1["Aa"])
    pygame.draw.rect(screen, pygame.Color(couleur["Ab"]), ligne1["Ab"])
    pygame.draw.rect(screen, pygame.Color(couleur["Ac"]), ligne1["Ac"])
    pygame.draw.rect(screen, pygame.Color(couleur["Ad"]), ligne1["Ad"])

    pygame.draw.rect(screen, pygame.Color(couleur["Ba"]), ligne2["Ba"])
    pygame.draw.rect(screen, pygame.Color(couleur["Bb"]), ligne2["Bb"])
    pygame.draw.rect(screen, pygame.Color(couleur["Bc"]), ligne2["Bc"])
    pygame.draw.rect(screen, pygame.Color(couleur["Bd"]), ligne2["Bd"])

    pygame.draw.rect(screen, pygame.Color(couleur["Ca"]), ligne3["Ca"])
    pygame.draw.rect(screen, pygame.Color(couleur["Cb"]), ligne3["Cb"])
    pygame.draw.rect(screen, pygame.Color(couleur["Cc"]), ligne3["Cc"])
    pygame.draw.rect(screen, pygame.Color(couleur["Cd"]), ligne3["Cd"])

    pygame.draw.rect(screen, pygame.Color(couleur["Da"]), ligne4["Da"])
    pygame.draw.rect(screen, pygame.Color(couleur["Db"]), ligne4["Db"])
    pygame.draw.rect(screen, pygame.Color(couleur["Dc"]), ligne4["Dc"])
    pygame.draw.rect(screen, pygame.Color(couleur["Dd"]), ligne4["Dd"])












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
        affichagel1 = True
    if keys[pygame.K_2]:
        verifyline2 = True
    if keys[pygame.K_3]:
        verifyline3 = True
    if keys[pygame.K_4]:
        verifyline4 = True




    #donner la vérification de la ligne 1: 
    if verifyline1 == True:

        resultline1 = verificationcode(code,reponseligne1)
        
        for i in range(0,(4 -len(resultline1))): 
            resultline1.append("grey")

        repcase1couleur[0] = resultline1[0]
        repcase1couleur[1] = resultline1[1]
        repcase1couleur[2] = resultline1[2]
        repcase1couleur[3] = resultline1[3]

        
    
        y = 350 #on met le pointer sur la ligne suivante 
        verifyline1 = False
    


    if affichagel1 == True:

        pygame.draw.rect(screen, pygame.Color(repcase1couleur[0]), repcase1[0])
        pygame.draw.rect(screen, pygame.Color(repcase1couleur[1]), repcase1[1])
        pygame.draw.rect(screen, pygame.Color(repcase1couleur[2]), repcase1[2])
        pygame.draw.rect(screen, pygame.Color(repcase1couleur[3]), repcase1[3])

























#rafraichissement de la page, puis timer afin que tout fonctionne bien avec les transitions
    pygame.display.update()
    timer.tick(10) #définition du timer à 60 images par secondes 



