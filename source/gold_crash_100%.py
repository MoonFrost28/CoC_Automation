import sys
import time

from variables import farm_gold, collect_elixir_cart, quit_game

# Temporisation de 3 secondes avant de lancer le script
time.sleep(3)

try:
    # Fonction principale
    def executer_script(nb_boucles):
        # Exécute la fonction de farm de gold nb_boucles fois
        for _ in range(nb_boucles):
            farm_gold()
            time.sleep(1)
            #quit_game()
            time.sleep(1)
            # Récupération de la charrette d'élixir
            collect_elixir_cart(nb_boucles)

    nb_boucles = int(sys.argv[1])
    executer_script(nb_boucles)

except KeyboardInterrupt:
    print("Le script a été interrompu par l'utilisateur.")