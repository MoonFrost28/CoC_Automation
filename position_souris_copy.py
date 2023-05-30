from pynput.mouse import Controller, Button, Listener
from pynput import keyboard

print('Cliquez sur l\'écran pour afficher les coordonnées.')

# Créez une variable globale pour suivre l'état d'arrêt
stopped = False

# Créez une fonction pour arrêter l'écoute du clavier
def stop_listener():
    global stopped
    stopped = True

# Définissez une fonction de rappel pour les clics de souris
def on_click(x, y, button, pressed):
    if pressed:
        print('Position souris : ({0}, {1})'.format(x, y))

# Définissez une fonction de rappel pour la pression de la touche
def on_press(key):
    if key == keyboard.Key.q:
        stop_listener()

# Créez des écouteurs pour la souris et le clavier
mouse_listener = Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

# Démarrez les écouteurs
mouse_listener.start()
keyboard_listener.start()

# Attendez que l'utilisateur appuie sur la touche 'q' pour arrêter
while not stopped:
    pass

# Arrêtez les écouteurs
mouse_listener.stop()
keyboard_listener.stop()