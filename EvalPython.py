from colorama import init
init()
from colorama import Fore, Back, Style


from random import*
bibliotheque = ['BLONDE', 'CALMER', 'VAPEUR', 'DINGUE', 'ZOMBIE', 'VALISE', 'VIOLET', 'THUNES', 'TAQUIN', 'STYLOS']
mot = ['.', '.', '.', '.', '.', '.']

motMystere=choice(bibliotheque)

essais = 8

print("Bienvenue dans MOTUS ! Vous devez trouver le mot mystère en fonction du placement de vos lettres. A vous de jouer !")
print("Veuillez entrer un mot de 6 lettres (en majuscule)")
motChoisit = input ()

def lettreCommunes(motMystere, motChoisit):
    for lettre in motMystere:
        if lettre in motChoisit:
            print (Back.RED + lettre)
    
            
print("les lettres affichées en rouge sont les lettres communes entre votre mot et le mot mystère")

lettreCommunes(motMystere, motChoisit)
print(Style.RESET_ALL)


print("veuillez à nouveau entrer un mot en tenant compte de ces indications")
motChoisit = input ()

lettreCommunes(motMystere, motChoisit)
print(Style.RESET_ALL)

print("veuillez à nouveau entrer un mot en tenant compte de ces indications")
motChoisit = input ()

lettreCommunes(motMystere, motChoisit)
print(Style.RESET_ALL)

print("veuillez à nouveau entrer un mot en tenant compte de ces indications")
motChoisit = input ()

lettreCommunes(motMystere, motChoisit)
print(Style.RESET_ALL)

print("veuillez à nouveau entrer un mot en tenant compte de ces indications")
motChoisit = input ()

lettreCommunes(motMystere, motChoisit)
print(Style.RESET_ALL)

print("veuillez à nouveau entrer un mot en tenant compte de ces indications")
motChoisit = input ()

lettreCommunes(motMystere, motChoisit)
print(Style.RESET_ALL)

print("veuillez à nouveau entrer un mot en tenant compte de ces indications")
motChoisit = input ()

lettreCommunes(motMystere, motChoisit)
print(Style.RESET_ALL)

print("veuillez à nouveau entrer un mot en tenant compte de ces indications")
motChoisit = input ()

lettreCommunes(motMystere, motChoisit)
print(Style.RESET_ALL)

print("Vous avez utilisé toutes vos chances, désolé")

input ()


