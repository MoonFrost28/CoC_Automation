import sys
import time

from Functions import farm_elixir, collect_elixir_cart

# Temporisation de 3 secondes avant de lancer le script
time.sleep(3)

try:
    # Fonction principale
    def executer_script(nb_boucles):
        # Exécute la fonction de farm d'elixir nb_boucles fois
        for _ in range(nb_boucles):
            farm_elixir()
            time.sleep(1.1)  # Temporisation de 1.1 secondes entre chaque série de touches
        
        # Récupération de la charrette d'élixir
        collect_elixir_cart(nb_boucles, False)

    nb_boucles = int(sys.argv[1])
    nb_iterations = int(sys.argv[2])
    for _ in range(nb_iterations):
        executer_script(nb_boucles)
        time.sleep(2)  # Temporisation de 2 secondes entre chaque itération

except KeyboardInterrupt:
    print("Le script a été interrompu par l'utilisateur.")