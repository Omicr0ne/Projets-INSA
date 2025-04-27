from turtle import *
from random import *
import math

# Procedures de bases :

def rectangle(hauteur : int, largeur : int, couleurR : str):
    '''Dessine un rectangle d'une certaine hauteur, largeur et couleur'''
    
    # Variables locales
    i : int
    
    down()
    color(couleurR)        # On définit la couleur du stylo et du remplissage
    begin_fill()
    for i in range(2):
        fd(largeur)
        lt(90)
        fd(hauteur)
        lt(90)
    end_fill()
    up()

def hexagone(taille : int, couleurH : int):
    '''Dessine un hexagone avec une longeure de coté et une couleur définie, cette procedure n'est finalement pas utilisé'''

    # Variables locales
    i : int

    color(couleurH)
    down()
    begin_fill()
    for i in range(6):
        fd(taille)
        lt(60)
    end_fill()
    up()

def triangle(a:int, b:int , c:int, CouleurT:str):
    """a, b, c : correspondent aux cotés du triangle et la couleur est à définir"""

    # Calculer les cosinus des angles (lois des cosinus)
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)

    # Convertir les cosinus en angles en radians
    angle_A_rad = math.acos(cos_A)
    angle_B_rad = math.acos(cos_B)
    angle_C_rad = math.acos(cos_C)

    # Convertir les angles en degrés
    angle_A = 180 - math.degrees(angle_A_rad) 
    angle_B = 180 - math.degrees(angle_B_rad)
    angle_C = 180 - math.degrees(angle_C_rad)
    
    color(CouleurT)
    down()
    begin_fill()
    forward(a)
    left(angle_C)
    forward(b)
    left(angle_A)
    forward(c)
    left(angle_B)
    end_fill()
    up()

def cercle(r : int, couleurC : str):
    '''Dessine un cercle de rayon r et d'une couleur à définir'''

    color(couleurC)
    down()
    begin_fill()
    down()
    circle(r)
    end_fill()
    up()

def étoile(taille:int, nbr:int, couleurE:str):
    '''Dessine une étoile avec un certain nombre de branche, une taille et une couleur'''

    b :int = 160
    a :float =   360/nbr - b
    i : int
    j : float
    
    color(couleurE)
    begin_fill()
    down()
    for i in range(0, nbr):
        for j in range(0, 2):
            forward(taille)
            right(b)
        left(b)
        right(a)
    end_fill()
    up()


# procedures complexes :

def carré(c : int, couleurC : str):
    '''dessine un carré de coté c'''

    rectangle(c,c,couleurC)

def immeuble(étages : int, largeur : int, couleurI : str):
    '''dessine un immeuble avec un nombre d'étages, une largeur et une couleur défini'''

    # variables locales
    valeurEtage : int = 80+(40*(étages-1))                  # Donne la hauteur de l'immeuble en pixel en fonction du nombre d'étages souhaités.
    valeurLargeur : int = 60+(40*(largeur-1))               # Donne la largeur de l'immeuble en pixel en fonction du nombre d'appartements souhaités.
    hauteur : int
    appart : int
    toit : bool = choice([True,False])                      # Défini si la maison aura un toit triangulaire
    probabilite : int
    yEtoile : int = randint(44,abs(600-valeurEtage))        # Défini la position en y de l'étoile au dessus de l'immeuble
    xEtoile : int = randint(24,valeurLargeur-24)            # Défini la position en x de l'étoile au dessus de l'immeuble
 
    down()
    rectangle(valeurEtage, valeurLargeur, couleurI)
    if toit and étages <= 2 and largeur <= 3:
        up()
        lt(90)
        fd(valeurEtage)
        rt(90)
        down()
        triangle(valeurLargeur, valeurLargeur*0.54, valeurLargeur*0.54, couleurI)
        up()
        rt(90)
        fd(valeurEtage)
        lt(90)
    up()
    fd((valeurLargeur/2)-20)
    rectangle(30,40,'blue')
    bk((valeurLargeur/2)-20)
    lt(90)
    fd(valeurEtage-40)
    rt(90)
    fd(20)
    for hauteur in range(étages):               # Boucle permettant de passer à l'étage inférieur
        for appart in range(largeur):           # Boucle permettant de passer à l'appartement de doite
            probabilite = randint(1, 8)
            if probabilite == 1:                # Détermine si la lumière est allumé ou éteinte
                carré(20,'black')
                fd(40)
            else:
                carré(20,'yellow')
                fd(40)
        bk(largeur*40)
        rt(90)
        fd(40)
        lt(90)
    fd(valeurLargeur-20)
    lt(90)
    fd(valeurEtage + yEtoile)
    rt(90)
    bk(xEtoile)
    étoile(randint(8 , 12), randint(4, 8), "white")     # Dessine l'étoile à la position courante (déterminé aléatoirement)
    fd(xEtoile)
    rt(90)
    fd(valeurEtage + yEtoile)
    lt(90)

def skyline():
    '''dessine une skyline avec des dimmentions d'immeubles aléatoires'''

    # variables locales
    couleursImmeubles = ['#7B241C','#7E5109','#34495E']     # Les couleurs que peuvent prendre les immeubles

    up()
    goto(-960,-220)                                         # Positionne le curseur sur le coté gauche d'un écran full hd, la moitier de la largeur d'un écran full HD est 960 pixels
    while xcor() < 960:                                     # Dessine des immeubles tant que le curseur est dans l'écran
        immeuble(randint(2, 12), randint(2, 5), choices(couleursImmeubles))

def trottoir(taille : int):
    '''dessine le trottoir avec d'une certaine épaisseur'''
    
    up()
    goto(-960,-241-taille)              # Positionne le curseur sur le coté gauche d'un écran full hd
    down()
    rectangle(20+taille,1920,'grey')
    up()
    goto(-960,-442-taille)              # Positionne le curseur sur le coté gauche d'un écran full hd
    down()
    rectangle(20+taille,1920,'grey')

def route(taille : int):
    '''dessine la route avec une certaine épaisseur'''
    
    # variables
    xpos : int = -960           # Positionne le curseur sur le coté gauche d'un écran full hd
    ypos : int = -401-taille    # Positionne le curseur à la hauteur voulu
    y : int = 160+taille        # Positionne le curseur à la hauteur voulu en fonction de la taille

    up()
    goto(xpos,ypos)
    down()
    rectangle(y,1920,'black')
    up()
    goto(xpos+5,((ypos)+(y)/2)-10)
    while xcor() < 920:             # Dessine le marquage au sol tant que le curseur est dans l'écran
        rectangle(5,30,'white')
        up()
        fd(52)

def lune(x : int, y : int):
    '''dessine la lune à une certaine position x, y'''

    up()
    goto(x,y)
    cercle(40,'white')
    

# tableau

def tableau():
    '''dessine le tableau'''

    ht()                # Cache le curseur
    speed(0)
    bgcolor('#002240')
    route(20)
    trottoir(10)
    lune(-875,390)
    skyline()


# programme principale :

tableau()
exitonclick()