import sys
import time

from variables import farm_elixir, collect_elixir_cart

# Temporisation de 3 secondes avant de lancer le script
time.sleep(3)

try:
    # Fonction principales
    def executer_script(nb_boucles, nb_iterations, current_iteration):
        total_loops = nb_boucles * nb_iterations
        # Exécute la fonction de farm d'elixir nb_boucles fois
        for _ in range(nb_boucles):
            farm_elixir()
            current_loop = _ + 1
            current_loop_in_iteration = current_loop + current_iteration * nb_boucles
            print(str(current_loop) + '/' + str(nb_boucles) + '     ' + 
                str(current_loop_in_iteration) + '/' + str(total_loops))
            time.sleep(1.1)  # Temporisation de 1.1 secondes entre chaque série de touches
        
        # Récupération de la charrette d'élixir
        collect_elixir_cart(nb_boucles, True)

    # Vérifier si le nombre de boucles et l'instruction de réexécution sont spécifiés en argument de ligne de commande
    if len(sys.argv) > 2:
        try:
            nb_boucles = int(sys.argv[1])
            nb_iterations = int(sys.argv[2])
            for _ in range(nb_iterations):
                executer_script(nb_boucles, nb_iterations, _)
                time.sleep(2)  # Temporisation de 2 secondes entre chaque itération
            print("Le script elixir s'est exécuté avec succès.")
        except ValueError:
            print("Veuillez spécifier un nombre entier de boucles.")
    else:
        nb_boucles = 1
        nb_iterations = 1
        current_iteration = 1
        executer_script(nb_boucles, nb_iterations, current_iteration)
        print("Le script elixir s'est exécuté avec succès.")
except KeyboardInterrupt:
    print("Le script a été interrompu par l'utilisateur.")