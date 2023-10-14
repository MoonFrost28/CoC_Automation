import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QProgressBar
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, QThread, pyqtSignal

def execute_gold():
    nb_boucles = gold_nb_boucles_entry.text()
    if nb_boucles=="":
        nb_boucles = str(1)
        loop_text = "loop"
    else:
        loop_text = "loops"
    print("Executing gold script with", nb_boucles, loop_text)
    script_path = "source/gold_crash_100%.py"
    subprocess.run(["python", script_path, nb_boucles])

def execute_elixir():
    nb_boucles = elixir_nb_boucles_entry.text()
    nb_iterations = elixir_nb_iterations_entry.text()
    if nb_boucles=="":
        nb_boucles = str(1)
        loop_text = "loop"
    else:
        loop_text = "loops"
    if nb_iterations=="":
        nb_iterations = str(1)
        iteration_text = "iteration"
    else:
        iteration_text = "iterations"        
    print("Executing elixir script with", nb_boucles, loop_text, "and", nb_iterations, iteration_text)
    script_path = "source/elixir.py"
    subprocess.run(["python", script_path, nb_boucles, nb_iterations])


def execute_trophy_drop():
    nb_boucles = trophy_drop_nb_boucles_entry.text()
    if nb_boucles=="":
        nb_boucles = str(1)
        loop_text = "loop"
    else:
        loop_text = "loops"
    print("Executing trophy_drop script with", nb_boucles, loop_text)
    script_path = "source/trophy_drop.py"
    subprocess.run(["python", script_path, nb_boucles])


def exit_application():
    app.quit()

# Création de l'application PyQt
app = QApplication(sys.argv)

# Création de la fenêtre principale
window = QWidget()
window.setWindowTitle("Clash of Clans script")
window.setGeometry(100, 100, 400, 100)
app.setWindowIcon(QIcon("Images/CoC_icon.ico"))

# Création des layouts pour organiser les éléments
main_layout = QVBoxLayout()
button_layout = QHBoxLayout()
entry_layout = QHBoxLayout()
elixir_layout = QVBoxLayout()
gold_layout = QVBoxLayout()
trophy_drop_layout = QVBoxLayout()
exit_layout = QHBoxLayout()

# Création des icônes à partir des fichiers d'images
gold_pixmap = QPixmap("Images/GoldB.png")
gold_icon = QIcon(gold_pixmap)

elixir_pixmap = QPixmap("Images/ElixirB.png")
elixir_icon = QIcon(elixir_pixmap)

diamond_pixmap = QPixmap("Images/Diamond_LeagueB.png")
diamond_icon = QIcon(diamond_pixmap)

icon = QIcon("Images/CoC_icon.ico")

# Création des boutons avec les icônes correspondantes
gold_button = QPushButton("Gold")
gold_button.setIcon(gold_icon)
gold_button.clicked.connect(execute_gold)
gold_button.setIconSize(QSize(20, 20))
gold_button.setStyleSheet("QPushButton {"
                          "     text-align: center;"
                          "     font-size: 14px;"
                          "}")

elixir_button = QPushButton("Elixir")
elixir_button.setIcon(elixir_icon)
elixir_button.clicked.connect(execute_elixir)
elixir_button.setIconSize(QSize(20, 20))
elixir_button.setStyleSheet("QPushButton {"
                          "     text-align: center;"
                          "     font-size: 14px;"
                          "}")

trophy_drop_button = QPushButton("Trophy Drop")
trophy_drop_button.setIcon(diamond_icon)
trophy_drop_button.clicked.connect(execute_trophy_drop)
trophy_drop_button.setIconSize(QSize(20, 20))
trophy_drop_button.setStyleSheet("QPushButton {"
                          "     text-align: center;"
                          "     font-size: 14px;"
                          "}")

exit_button = QPushButton("Exit")
exit_button.clicked.connect(exit_application)

# Ajout des boutons au layout des boutons
button_layout.addWidget(gold_button)
button_layout.addWidget(elixir_button)
button_layout.addWidget(trophy_drop_button)

# Ajout des labels au layout des labels
gold_nb_boucles_label = QLabel("Gold loops number :")
elixir_nb_boucles_label = QLabel("Elixir loops number :")
elixir_nb_iterations_label = QLabel("Elixir iterations number :")
trophy_drop_nb_boucles_label = QLabel("Trophy Drop loops number:")

# Création des zones d'entrée
gold_nb_boucles_entry = QLineEdit()
gold_nb_boucles_entry.setPlaceholderText("Enter a number...")

elixir_nb_boucles_entry = QLineEdit()
elixir_nb_boucles_entry.setPlaceholderText("Enter a number...")

elixir_nb_iterations_entry = QLineEdit()
elixir_nb_iterations_entry.setPlaceholderText("Enter a number...")

trophy_drop_nb_boucles_entry = QLineEdit()
trophy_drop_nb_boucles_entry.setPlaceholderText("Enter a number...")

gold_layout.addWidget(gold_nb_boucles_label)
gold_layout.addWidget(gold_nb_boucles_entry)
gold_layout.addStretch()

elixir_layout.addWidget(elixir_nb_boucles_label)
elixir_layout.addWidget(elixir_nb_boucles_entry)
elixir_layout.addStretch()
elixir_layout.addWidget(elixir_nb_iterations_label)
elixir_layout.addWidget(elixir_nb_iterations_entry)
elixir_layout.addStretch()

trophy_drop_layout.addWidget(trophy_drop_nb_boucles_label)
trophy_drop_layout.addWidget(trophy_drop_nb_boucles_entry)
trophy_drop_layout.addStretch()

# Ajout des zones d'entrée au layout des zones d'entrée
entry_layout.addLayout(gold_layout)
entry_layout.addLayout(elixir_layout)
entry_layout.addLayout(trophy_drop_layout)

main_layout.addLayout(button_layout)
main_layout.addLayout(entry_layout)

# Ajout du bouton Exit au layout de sortie
exit_layout.addStretch()
exit_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Widget vide extensible
exit_layout.addWidget(exit_button)

# Ajout du layout de sortie au layout principal
main_layout.addLayout(exit_layout)

# Définition du layout principal pour la fenêtre
window.setLayout(main_layout)

# Affichage de la fenêtre
window.show()

# Exécution de l'application PyQt
sys.exit(app.exec_())
