#########################################################################
#              Importations des modules
#########################################################################



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

game_on = True #variable qui définit que le jeu est allumé
game_won = False # variable for when game is won

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
        global game_on
        game_on = False
        global game_won
        game_won = True
        
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

screen = pygame.display.set_mode((1100,850)) #definition de la taille de la fenêtre (ex: 400x500) #c'est une surface primaire, le display surface est unique
timer = pygame.time.Clock() #definition de la fonction qui définit le nombre d'image par seconde (raffraichissement du jeu)



#################################################################################################################
#################################################################################################################



banniere =pygame.Rect(0,0,1100,40) #definition d'une surface ou l'on affichera du texte ou le titre

nombre_essais = 0 

###########################################################################################################
#definition des cases: 


#definition de la position de cases


matrice = {}
for i in range(8):
    for j in range(4):
        matrice[str(i) + str(j)] = pygame.Rect((j+2)*100 + 50, (i+2)*100 -150 , 50,50) 

#definition des couleurs des cases, l'utilisation des dictionnaires est très importante
matrice_couleur = {}
for i in range(8):
    for j in range(4):
        matrice_couleur[str(i) + str(j)] = "blue"
   

############################################################################################
#definition des cases de réponses
###########################################################################################
repcase = {}
for i in range(8):
    for j in range(4):
        repcase[str(i)+str(j)] = pygame.Rect((j+7)*100,(i+2)*100-150,50,50)
        

repcasecouleur = {}
for i in range(8):
    for j in range(4):
        repcasecouleur[str(i)+str(j)] = "white" # faute ici voir result first line

#Position de base du pointer

x = 250
y = 50

##################################################################################
#les verifications des lignes sont éteintes de base
##################################################################################

verifyline0 = False
verifyline1 = False
verifyline2 = False
verifyline3 = False
verifyline4 = False
verifyline5 = False
verifyline6 = False
verifyline7 = False

affichagel0 = False
affichagel1 = False
affichagel2 = False
affichagel3 = False
affichagel4 = False
affichagel5 = False
affichagel6 = False
affichagel7 = False

resultline0 = []
resultline1 = []
resultline2 = []
resultline3 = []
resultline4 = []
resultline5 = []
resultline6 = []
resultline7 = []

### MAIN LOOP ######

while game_on == True:
        

    pointer = pygame.Rect(x,y,50,50)
    for event in pygame.event.get():  #Pour chaque élément qu'il se passe lors du fonctionnement du jeu pygame: 
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() #permet de quitter le programme quand on appuie sur la croix rouge, le sys exit est nécessaire pour que le programme s'arrête complètement


    screen.fill(pygame.Color("grey")) #on veut un display screen de couleur blanche


    pygame.draw.rect(screen, pygame.Color("red"), banniere) #on dessine la bannière
    #titre
    font_mastermind = pygame.font.SysFont(None, 24)
    mm_img = font_mastermind.render("Mastermind: ", True, pygame.Color("white"))
    screen.blit(mm_img, (20, 20))
    #instructions
    font_instr = pygame.font.SysFont(None, 20)
    instr_img = font_instr.render("enter the first letter of color (r,o,y,g,b,p) and confirm with line number", True, pygame.Color("white"))
    screen.blit(instr_img,(120,22))
    #numérotation lignes
    numeros_font = pygame.font.SysFont(None, 24)
    number_list = []
    for i in range(8):
        numero = numeros_font.render(str(i), True, pygame.Color("white"))
        screen.blit(numero, (200,i*100+67))

    
    for i in range(8):
        for j in range(4):
            pygame.draw.rect(screen, pygame.Color(matrice_couleur[str(i) + str(j)]), matrice[str(i) + str(j)])



    pygame.draw.rect(screen, pygame.Color("black"), pointer, 3)



#Pour obtenir les données du clavier:
    keys = pygame.key.get_pressed()


#Pour faire bouger le pointer de gauche à droite: 
    if keys[pygame.K_LEFT] and x>250:
        x = x - 100
    if keys[pygame.K_RIGHT] and x<550:
        x = x + 100


#Pour connaître la case sélectionnée par le pointer
    for i in range(8):
        for j in range(4):
            if matrice[str(i)+str(j)] == pygame.Rect(x,y,50,50):
                selection = str(i)+str(j)


    ####################################################################################
    #Changements de couleur avec les touches
    #####################################################################################
    if keys[pygame.K_b]:
        matrice_couleur[selection] = "blue"

    if keys[pygame.K_g]: 
        matrice_couleur[selection] = "green"

    if keys[pygame.K_y]:
        matrice_couleur[selection] = "yellow"

    if keys[pygame.K_r]: 
        matrice_couleur[selection] = "red"

    if keys[pygame.K_o]:
        matrice_couleur[selection] = "orange"

    if keys[pygame.K_p]:
        matrice_couleur[selection] = "pink"


###################################################################################
#décodage de la séquence des lignes:
#reponseligne est égal à l'entrée de l'utilisateur
###################################################################################

        
    reponseligne0 = []
    for i in range(4):
        reponseligne0.append(matrice_couleur["0"+str(i)])
     
    reponseligne1 = []
    for i in range(4):
        reponseligne1.append(matrice_couleur["1"+str(i)])
    
    reponseligne2 = []
    for i in range(4):
        reponseligne2.append(matrice_couleur["2"+str(i)])

    reponseligne3 = []
    for i in range(4):
        reponseligne3.append(matrice_couleur["3"+str(i)])
    
    reponseligne4 = []
    for i in range(4):
        reponseligne4.append(matrice_couleur["4"+str(i)])

    reponseligne5 = []
    for i in range(4):
        reponseligne5.append(matrice_couleur["5"+str(i)])
     
    reponseligne6 = []
    for i in range(4):
        reponseligne6.append(matrice_couleur["6"+str(i)])
    
    reponseligne7 = []
    for i in range(4):
        reponseligne7.append(matrice_couleur["7"+str(i)])
 
   
    
    
    ##########################################

#clavier pour vérifier les lignes:
    if keys[pygame.K_0]:
        verifyline0 = True
        affichagel0 = True
        nombre_essais = 1
    if keys[pygame.K_1]:
        verifyline1 = True
        affichagel1 = True
        nombre_essais = 2
    if keys[pygame.K_2]:
        verifyline2 = True
        affichagel2 = True
        nombre_essais = 3
    if keys[pygame.K_3]:
        verifyline3 = True
        affichagel3 = True
        nombre_essais = 4
    if keys[pygame.K_4]:
        verifyline4 = True
        affichagel4 = True
        nombre_essais = 5
    if keys[pygame.K_5]:
        verifyline5 = True
        affichagel5 = True
        nombre_essais = 6
    if keys[pygame.K_6]:
        verifyline6 = True
        affichagel6 = True
        nombre_essais = 7
    if keys[pygame.K_7]:
        verifyline7 = True
        affichagel7 = True
        nombre_essais = 8
    

#donner la vérification de la ligne 0: 
    if verifyline0 == True:
        n=1

        resultline0 = verificationcode(code,reponseligne0)
        
        for i in range(0,(4 -len(resultline0))): 
            resultline0.append("grey")

        for i in range(4):
            repcasecouleur["0" + str(i)] = resultline0[i]
            
        verifyline0 = False
        y = 150 #on met le pointer sur la ligne suivante
        
         

#affichage de la correction de la ligne 0: 
    if affichagel0 == True:
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(repcasecouleur["0" + str(i)]), repcase["0" + str(i)])


#donner la vérification de la ligne 1: 
    if verifyline1 == True:
        n=2
        
        resultline1 = verificationcode(code,reponseligne1)
        
        for i in range(0,(4 -len(resultline1))): 
            resultline1.append("grey")

        for i in range(4):
            repcasecouleur["1" + str(i)] = resultline1[i]
        
        y = 250 #on met le pointer sur la ligne suivante 
        verifyline1 = False
        
    

#affichage de la correction de la ligne 1: 
    if affichagel1 == True:
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(repcasecouleur["1" + str(i)]), repcase["1" + str(i)])

#donner la vérification de la ligne 2: 
    if verifyline2 == True:
        n=3
        resultline2 = verificationcode(code,reponseligne2)
        
        for i in range(0,(4 -len(resultline2))): 
            resultline2.append("grey")

        for i in range(4):
            repcasecouleur["2" + str(i)] = resultline2[i]
        
        y = 350 #on met le pointer sur la ligne suivante 
        verifyline2 = False
    

#affichage de la correction de la ligne 2: 
    if affichagel2 == True:
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(repcasecouleur["2" + str(i)]), repcase["2" + str(i)])

#donner la vérification de la ligne 3: 
    if verifyline3 == True:
        n=4
        resultline3 = verificationcode(code,reponseligne3)
        
        for i in range(0,(4 -len(resultline3))): 
            resultline3.append("grey")

        for i in range(4):
            repcasecouleur["3" + str(i)] = resultline3[i]
        
        y = 450 #on met le pointer sur la ligne suivante 
        verifyline3 = False
    

#affichage de la correction de la ligne 3: 
    if affichagel3 == True:
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(repcasecouleur["3" + str(i)]), repcase["3" + str(i)])

#donner la vérification de la ligne 4: 
    if verifyline4 == True:

        resultline4 = verificationcode(code,reponseligne4)
        
        for i in range(0,(4 -len(resultline4))): 
            resultline4.append("grey")

        for i in range(4):
            repcasecouleur["4" + str(i)] = resultline4[i]
        
        y = 550 #on met le pointer sur la ligne suivante 
        verifyline4 = False
    

#affichage de la correction de la ligne 4: 
    if affichagel4 == True:
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(repcasecouleur["4" + str(i)]), repcase["4" + str(i)])

#donner la vérification de la ligne 5: 
    if verifyline5 == True:
        n=6
        resultline5 = verificationcode(code,reponseligne5)
        
        for i in range(0,(4 -len(resultline5))): 
            resultline5.append("grey")

        for i in range(4):
            repcasecouleur["5" + str(i)] = resultline5[i]
        
        y = 650 #on met le pointer sur la ligne suivante 
        verifyline5 = False
    

#affichage de la correction de la ligne 5: 
    if affichagel5 == True:
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(repcasecouleur["5" + str(i)]), repcase["5" + str(i)])


#donner la vérification de la ligne 6: 
    if verifyline6 == True:
        n=7
        resultline6 = verificationcode(code,reponseligne6)
        
        for i in range(0,(4 -len(resultline6))): 
            resultline6.append("grey")

        for i in range(4):
            repcasecouleur["6" + str(i)] = resultline6[i]
        
        y = 750 #on met le pointer sur la ligne suivante 
        verifyline6 = False
    

#affichage de la correction de la ligne 6: 
    if affichagel6 == True:
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(repcasecouleur["6" + str(i)]), repcase["6" + str(i)])

#donner la vérification de la ligne 7: 
    if verifyline7 == True:
        n=8
        resultline7 = verificationcode(code,reponseligne7)
        
        for i in range(0,(4 -len(resultline7))): 
            resultline7.append("grey")

        for i in range(4):
            repcasecouleur["7" + str(i)] = resultline7[i]
        
        y = 850 #on met le pointer sur la ligne suivante 
        verifyline7 = False
    

#affichage de la correction de la ligne 7: 
    if affichagel7 == True:
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(repcasecouleur["7" + str(i)]), repcase["7" + str(i)])



#rafraichissement de la page, puis timer afin que tout fonctionne bien avec les transitions
    pygame.display.update()
    timer.tick(10) #définition du timer à 60 images par secondes 


while game_won == True:
    screen.fill(pygame.Color("white"))
    font = pygame.font.SysFont(None, 80)
    img = font.render(("Vous avez gagné en " + str(nombre_essais) + " essais"), True, pygame.Color("blue"))
    screen.blit(img, (5, 50))
    pygame.display.update()
    for event in pygame.event.get():  #Pour chaque élément qu'il se passe lors du fonctionnement du jeu pygame: 
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() 
    






