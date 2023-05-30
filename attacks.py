import pyautogui, time

def attack_and_drop():
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
