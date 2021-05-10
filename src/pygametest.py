import pygame #module pygame 
import sys #module nécessaire pour bien fermer le programme


pygame.init() #initialisation du module pygame (indispensable)

screen = pygame.display.set_mode((400,500)) #definition de la taille de la fenêtre (ex: 400x500) #c'est une surface primaire, le display surface est unique
timer = pygame.time.Clock() #definitiion de la fonction qui définit le nombre d'image par seconde (raffraichissement du jeu)

my_surface =pygame.Surface((100,100)) #definition d'une surface





game_on = True #variable qui définit que le jeu est allumé

while game_on == True:
    for event in pygame.event.get():  #Pour chaque élément qu'il se passe lors du fonctionnement du jeu pygame: 
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() #permet de quitter le programme quand on appuie sur la croix rouge, le sys exit est nécessaire pour que le programme s'arrête complètement
    
    screen.fill(pygame.Color("white")) #on veut un display screen de couleur blanche
    screen.blit(my_surface, (150,200)) #150 et 200 représentent les coordonnées x et y du coins en haut à gauche

    pygame.display.update()
    timer.tick(60) #définition du timer à 60 images par secondes 

    eee

