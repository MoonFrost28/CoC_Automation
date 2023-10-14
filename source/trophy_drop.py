import sys
import time

from Functions import farm_elixir, collect_elixir_cart, change_village, reset_village

# Temporisation de 3 secondes avant de lancer le script
time.sleep(3)

try:
    # Fonction principale
    def executer_script(nb_boucles):
        # Passe au village "open"
        change_village()

        # Exécute la fonction de farm d'elixir nb_boucles fois - utilisé seulement pour perdre des trophées
        for _ in range(nb_boucles):
            farm_elixir()
            time.sleep(1.1)  # Temporisation de 1.1 secondes entre chaque série de touches
            if _ % 10 == 0: # Récupère la charrette toutes les 10 boucles
                collect_elixir_cart(nb_boucles)

        # Réinitialise le village initial
        reset_village()

    nb_boucles = int(sys.argv[1])
    executer_script(nb_boucles)
    
except KeyboardInterrupt:
    print("Le script a été interrompu par l'utilisateur.")