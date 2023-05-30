import sys
import time
import keyboard
import pyautogui

# Combinaison de touches pour interrompre le code
combinaison_interruption = ['q']

# Fonction pour vérifier si la combinaison de touches est enfoncée
def check_combinaison_touche():
    return keyboard.is_pressed(combinaison_interruption[0])

# Temporisation de 3 seconsdes
time.sleep(3)

#List des touches init
touche_init = ['p', 'd', 'u', 'x']

# Liste des touches à répéter
serie_touche = ['num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7']

# Liste des touches supplémentaires
touches_supplementaires = ['subtract', 'num9', 'num0', 'num5']

# Liste des touches reset
touches_reset = ['p', 's', 'u', 'x']

# Durées de temporisation spécifiques pour chaque touche
temporisation_touche = {
    'd' : 0.4, # Temporisation de 0.5 seconde pour la touche "d"
    'num2': 3.5, # Temporisation de 3.5 secondes pour la touche "num2"
    'num6': 0.25, # Temporisation de 0.25 seconde pour la touche "num6"
    'num7' : 1, # Temporisation de 1 seconde pour la touche "num7"
    'subtract' : 0.4, # Temporisation de 0.4 seconde pour la touche "subtract"
    's' : 0.4 # Temporisation de 0.5 seconde pour la touche "s"
}

# Temporisation par défaut pour les touches non spécifiées dans le dictionnaire
temporisation_par_defaut = 0.04 # Temporisation de 40 millisecondes par défaut

# Variable pour vérifier si le script a été interrompu
interrompu = False

# Fonction principale
def executer_script(nb_boucles):
    global interrompu  # Déclarer la variable interrompu comme variable globale
    
    # Répétition de la série de touches
    for touche in touche_init:
        if check_combinaison_touche():  # Vérifier si la combinaison de touches est enfoncée
            interrompu = True
            break  # Sortir de la boucle interne si la combinaison de touches est détectée
        pyautogui.press(touche)
        if touche in temporisation_touche:
            temporisation = temporisation_touche[touche]
        else:
            temporisation = temporisation_par_defaut
        time.sleep(temporisation) 

    for _ in range(nb_boucles):
        for touche in serie_touche:
            if check_combinaison_touche():  # Vérifier si la combinaison de touches est enfoncée
                interrompu = True
                break  # Sortir de la boucle interne si la combinaison de touches est détectée
            pyautogui.press(touche)
            if touche in temporisation_touche:
                temporisation = temporisation_touche[touche]
            else:
                temporisation = temporisation_par_defaut
            time.sleep(temporisation)
        if _ % 10 == 0:
            for touche in touches_supplementaires:
                if check_combinaison_touche():  # Vérifier si la combinaison de touches est enfoncée
                    interrompu = True
                    break  # Sortir de la boucle si la combinaison de touches est détectée
                if touche == 'subtract':
                    pyautogui.keyDown(touche)
                    time.sleep(0.5)
                    pyautogui.keyUp(touche)
                else:
                    pyautogui.press(touche)
                if touche in temporisation_touche:
                    temporisation = temporisation_touche[touche]
                else:
                    temporisation = temporisation_par_defaut
                time.sleep(temporisation)
        print(_ + 1)
        if interrompu:
            break  # Sortir de la boucle externe si la combinaison de touches est détectée
        time.sleep(1.1)  # Temporisation de 1,1 secondes entre chaque série de touches

    if not interrompu:
        # Exécution des touches supplémentaires
        for touche in touches_reset:
            if check_combinaison_touche():  # Vérifier si la combinaison de touches est enfoncée
                interrompu = True
                break  # Sortir de la boucle si la combinaison de touches est détectée
            pyautogui.press(touche)
            if touche in temporisation_touche:
                temporisation = temporisation_touche[touche]
            else:
                temporisation = temporisation_par_defaut
            time.sleep(temporisation)

# Vérifier si le nombre de boucles et l'instruction de réexécution sont spécifiés en argument de ligne de commande
if len(sys.argv) > 1:
    try:
        nb_boucles = int(sys.argv[1])
        executer_script(nb_boucles)
        if interrompu:
            print("Le script trophy_drop a été interrompu par l'utilisateur.")
        else:
            print("Le script trophy_drop s'est exécuté avec succès.")
    except ValueError:
        print("Veuillez spécifier un nombre entier de boucles.")
else:
    nb_boucles = 1
    executer_script(nb_boucles)
    print("Le script trophy_drop s'est exécuté avec succès.")
