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
elixir_cart = keys_config.elixir_cart

# Durées de temporisation spécifiques pour chaque touche
key_temporisation = {
  'find_attack': 3.5, # Temporisation de 3.5 secondes pour la touche "find_attack"
 'dezoom' : 0.4 # Temporisation de 0.4 seconde pour la touche "subtract"
}

# Temporisation par défaut pour les touches non spécifiées dans le dictionnaire
def_temporisation = 0.04 # Temporisation de 40 millisecondes par défaut

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
        for key in gold:
            if key == 'troops_drop':
                pyautogui.keyDown(gold[key])
                time.sleep(1)
                pyautogui.keyUp(gold[key])
            else:
                pyautogui.press(gold[key])
            if key in key_temporisation:
                temporisation = key_temporisation[key]
            else:
                temporisation = def_temporisation
            time.sleep(temporisation)
        time.sleep(1)
        #quit_game()

        # Exécution des touches supplémentaires
        for key in elixir_cart:
            if key == 'dezoom':
                pyautogui.keyDown(elixir_cart[key])
                time.sleep(0.5)
                pyautogui.keyUp(elixir_cart[key])
            else:
                pyautogui.press(elixir_cart[key])
            if key in key_temporisation:
                temporisation = key_temporisation[key]
            else:
                temporisation = def_temporisation
            time.sleep(temporisation)
            current_loop = _ + 1 
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
