from pynput.mouse import Listener

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
        print('Position souris : (X: {0}, Y: {1})'.format(x, y))

# Créez des écouteurs pour la souris et le clavier
mouse_listener = Listener(on_click=on_click)

# Démarrez les écouteurs
mouse_listener.start()

# Attendez que l'utilisateur appuie sur la touche 'q' pour arrêter
try:
    while not stopped:
        pass

    # Arrêtez les écouteurs
    mouse_listener.stop()

except KeyboardInterrupt:
    print ('\n')