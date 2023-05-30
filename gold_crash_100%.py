import sys
import time
import pyautogui
import importlib

import keys_config

# Temporisation de 3 secondes avant de lancer le script
time.sleep(3)

# Charger le fichier keys_config.py
keys_config = importlib.import_module('keys_config')

# Liste des touches à répéter
gold = keys_config.gold

# Liste des touches supplémentaires
elixir_cart = keys_config.elixir_cart

# Durées de temporisation spécifiques pour chaque touche
temporisation_touche = {
    'num2': 3.5, # Temporisation de 3.5 secondes pour la touche "num2"
    'subtract' : 0.4 # Temporisation de 0.4 seconde pour la touche "subtract"
}

# Temporisation par défaut pour les touches non spécifiées dans le dictionnaire
temporisation_par_defaut = 0.04 # Temporisation de 40 millisecondes par défaut

def quit_game():
    pyautogui.keyDown('ctrl') 
    pyautogui.keyDown('shift')
    pyautogui.press('5')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    pyautogui.click(1300, 130) # Coordonnées pour la touche "TOUT EFFACER"
    time.sleep(1)
    pyautogui.click(1080, 350) # Coordonnées pour l'application Clash of Clans
    time.sleep(16)

# Fonction principale
def executer_script(nb_boucles):
    # Répétition de la série de touches
    for _ in range(nb_boucles):
        for key in gold.values():
            if key == 'troops_drop':
                pyautogui.keyDown(key)
                time.sleep(1)
                pyautogui.keyUp(key)
            else:
                pyautogui.press(key)
            if key in temporisation_touche:
                temporisation = temporisation_touche[key]
            else:
                temporisation = temporisation_par_defaut
            time.sleep(temporisation)
        time.sleep(1)
        #quit_game()
        current_loop = _ + 1 

        # Exécution des touches supplémentaires
        for key in elixir_cart.values():
            if key == 'dezoom':
                pyautogui.keyDown(key)
                time.sleep(0.5)
                pyautogui.keyUp(key)
            else:
                pyautogui.press(key)
            if key in temporisation_touche:
                temporisation = temporisation_touche[key]
            else:
                temporisation = temporisation_par_defaut
            time.sleep(temporisation)
        print(str(current_loop) + '/' + str(nb_boucles))

# Vérifier si le nombre de boucles et l'instruction de réexécution sont spécifiés en argument de ligne de commande
if len(sys.argv) > 1:
    try:
        nb_boucles = int(sys.argv[1])
        executer_script(nb_boucles)
    except ValueError:
        print("Veuillez spécifier un nombre entier de boucles.")
else:
    nb_boucles = 1
    executer_script(nb_boucles)
    print("Le script gold s'est exécuté avec succès.")
