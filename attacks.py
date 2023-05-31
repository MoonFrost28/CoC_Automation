import pyautogui
import time
import importlib
import keys_config

keys_config = importlib.import_module('keys_config')

gold = keys_config.gold

elixir_cart = keys_config.elixir_cart

temporisation_touche = {
    'find_attack': 3.5,  # Temporisation de 3.5 secondes pour la touche "num2"
    'dezoom': 0.4  # Temporisation de 0.4 seconde pour la touche "subtract"
}

temporisation_par_defaut = 0.04

def attack_and_drop_gold():
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