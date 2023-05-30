import subprocess
import sys
import time

def main(nb_boucles_gold, nb_boucles_elixir, nb_iterations):

    # Récupérer les arguments en ligne de commande pour les fichiers à exécuter
    args_fichier1 = ['E:/Python/Macro_CoC/gold_crash_100%.py', nb_boucles_gold]
    args_fichier2 = ['E:/Python/Macro_CoC/elixir.py', nb_boucles_elixir, nb_iterations]


    # Lancement du premier fichier Python avec les arguments
    subprocess.run(['python'] + args_fichier1)

    time.sleep(1)
    
    # Lancement du deuxième fichier Python avec les arguments
    subprocess.run(['python'] + args_fichier2)


if len(sys.argv) > 3:
    try:   
        nb_boucles_gold = sys.argv[1]
        nb_boucles_elixir = sys.argv[2]
        nb_iterations = sys.argv[3]
        main(nb_boucles_gold, nb_boucles_elixir, nb_iterations)
    except ValueError:
        print("Veuillez spécifier un nombre entier de boucles.")
else:
    nb_boucles_gold = '1'
    nb_boucles_elixir = '1'
    nb_iterations = '1'
    main(nb_boucles_gold, nb_boucles_elixir, nb_iterations)
    print("Le script s'est exécuté avec succès.")