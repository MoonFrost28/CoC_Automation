import time
import pyautogui
import importlib

import keys_config

# Charger le fichier keys_config.py
keys_config = importlib.import_module('keys_config')

# Liste des touches à répéter
gold = keys_config.gold
elixir = keys_config.elixir
elixir_cart = keys_config.elixir_cart
village_swap = keys_config.village_swap
village_reset = keys_config.village_reset

# Durées de temporisation spécifiques pour chaque touche
key_temporisation = {
    'village_selection' : 0.5, # Temporisation de 0.5 seconde pour la touche "village_selection"
    'find_attack': 4,  # Temporisation de 3.5 secondes pour la touche "find_attack"
    'confirm': 0.25, # Temporisation de 0.25 seconde pour la touche "confirm"
    'dezoom' : 0.4 # Temporisation de 0.4 seconde pour la touche "dezoom"
}

# Temporisation par défaut pour les touches non spécifiées dans le dictionnaire
def_temporisation = 0.05 # Temporisation par défaut

def collect_elixir_cart(nb_boucles, activate_temporisation = False):
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
        if activate_temporisation:
            if key == "cart_click_2":
                tempo_sleep = 0.5 * nb_boucles
                time.sleep(tempo_sleep)
    time.sleep(0.05)

def farm_elixir():
    for key in elixir:
        pyautogui.press(elixir[key])
        if key in key_temporisation:
            temporisation = key_temporisation[key]
        else:
            temporisation = def_temporisation
        time.sleep(temporisation)
    time.sleep(0.1)

def farm_gold():
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
    time.sleep(0.05)

def change_village():
    for key in village_swap:
        pyautogui.press(village_swap[key])
        if key in key_temporisation:
            temporisation = key_temporisation[key]
        else:
            temporisation = def_temporisation
        time.sleep(temporisation)
    time.sleep(0.05)

def reset_village():
    for key in village_reset:
        pyautogui.press(village_reset[key])
        if key in key_temporisation:
            temporisation = key_temporisation[key]
        else:
            temporisation = def_temporisation
        time.sleep(temporisation)
    time.sleep(0.05)

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
    time.sleep(18)
    pyautogui.press('space')