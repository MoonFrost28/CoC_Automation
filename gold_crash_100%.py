import sys
import time

from variables import farm_gold, collect_elixir_cart, quit_game, display_loops

# Temporisation de 3 secondes avant de lancer le script
time.sleep(3)

try:
    # Fonction principale
    def executer_script(nb_boucles):
        # Exécute la fonction de farm de gold nb_boucles fois
        for _ in range(nb_boucles):
            farm_gold()
            time.sleep(1)
            quit_game()
            time.sleep(1)
            # Récupération de la charrette d'élixir
            collect_elixir_cart(nb_boucles)
            display_loops(_, nb_boucles)

    # Vérifier si le nombre de boucles et l'instruction de réexécution sont spécifiés en argument de ligne de commande
    if len(sys.argv) > 1:
        try:
            nb_boucles = int(sys.argv[1])
            executer_script(nb_boucles)
            print("Le script gold s'est exécuté avec succès.")
        except ValueError:
            print("Veuillez spécifier un nombre entier de boucles.")
    else:
        nb_boucles = 1
        executer_script(nb_boucles)
        print("Le script gold s'est exécuté avec succès.")
except KeyboardInterrupt:
    print("Le script a été interrompu par l'utilisateur.")