import sys
import time
import pyautogui

import keys_config

# Combinaison de touches pour interrompre le code
combinaison_interruption = ['q']

# Temporisation de 3 secondes
time.sleep(3)

# Liste des touches à répéter
key_sequence = keys_config.elixir_loop

# Liste des touches supplémentaires
touches_supplementaires = ['subtract', 'num8', 'num9', 'num0', 'num5']

# Durées de temporisation spécifiques pour chaque touche
temporisation_touche = {
    'num2': 3.5, # Temporisation de 3.5 secondes pour la touche "num2"
    'subtract' : 0.4 # Temporisation de 0.4 seconde pour la touche "subtract"
}

# Temporisation par défaut pour les touches non spécifiées dans le dictionnaire
temporisation_par_defaut = 0.04 # Temporisation de 40 millisecondes par défaut

# Variable pour vérifier si le script a été interrompu
interrompu = False

# Fonction principale
def executer_script(nb_boucles):
    global interrompu  # Déclarer la variable interrompu comme variable globale
    # Répétition de la série de touches
    for _ in range(nb_boucles):
        for touche in key_sequence:
            if touche == 'num4':
                pyautogui.keyDown(touche)
                time.sleep(1)
                pyautogui.keyUp(touche)
            else:
                pyautogui.press(touche)
            if touche in temporisation_touche:
                temporisation = temporisation_touche[touche]
            else:
                temporisation = temporisation_par_defaut
            time.sleep(temporisation)
        time.sleep(1)
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
        print(_ + 1)

        # Exécution des touches supplémentaires
        for touche in touches_supplementaires:
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
