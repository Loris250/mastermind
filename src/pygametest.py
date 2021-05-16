#########################################################################
#              Importations des modules
##########################################################################



import pygame #module pygame 
import sys #module nécessaire pour bien fermer le programme


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

Aa = pygame.Rect(250,250,50,50)
Ab = pygame.Rect(350,250,50,50)
Ac = pygame.Rect(450,250,50,50)
Ad = pygame.Rect(550,250,50,50)

colorAa = "blue"
colorAb = "blue"
colorAc = "blue"
colorAd = "blue"

x = 250
y = 250



game_on = True #variable qui définit que le jeu est allumé


while game_on == True:

    pointer = pygame.Rect(x,y,50,50)
    for event in pygame.event.get():  #Pour chaque élément qu'il se passe lors du fonctionnement du jeu pygame: 
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() #permet de quitter le programme quand on appuie sur la croix rouge, le sys exit est nécessaire pour que le programme s'arrête complètement


    screen.fill(pygame.Color("white")) #on veut un display screen de couleur blanche


    pygame.draw.rect(screen, pygame.Color("red"), banniere) #on dessine la bannière


    pygame.draw.rect(screen, pygame.Color(colorAa), Aa)
    pygame.draw.rect(screen, pygame.Color(colorAb), Ab)
    pygame.draw.rect(screen, pygame.Color(colorAc), Ac)
    pygame.draw.rect(screen, pygame.Color(colorAd), Ad)

    pygame.draw.rect(screen, pygame.Color("orange"), pointer, 3)


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - 100
    if keys[pygame.K_RIGHT]:
        x = x + 100






    pygame.display.update()
    timer.tick(10) #définition du timer à 60 images par secondes 



