import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QProgressBar
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, QThread, pyqtSignal

# Déclaration du thread d'exécution
class ExecutionThread(QThread):
    # Signal pour la progression de l'exécution
    execution_progress = pyqtSignal(int)

    def __init__(self, script_path, nb_boucles, nb_iterations=None):
        super().__init__()
        self.script_path = script_path
        self.nb_boucles = nb_boucles
        self.nb_iterations = nb_iterations 

    def run(self):
        command = ["python", self.script_path, self.nb_boucles]
        if self.nb_iterations is not None:
            command.append(self.nb_iterations)

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = process.communicate()  # Retrieve the output

        lines = output.decode().split("\n")  # Split the output into lines
        total_lines = len(lines)  # Count total lines in the output

        current_line = 0
        for line in lines:
            # Effectuer tout traitement nécessaire sur chaque ligne de sortie ici

            current_line += 1
            progress = int((current_line / total_lines) * 100)
            self.execution_progress.emit(progress)

# Création de l'application PyQt
app = QApplication(sys.argv)

# Création de la fenêtre principale
window = QWidget()
window.setWindowTitle("Clash of Clans script")
window.setGeometry(100, 100, 400, 200)
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
gold_button.setIconSize(QSize(20, 20))
gold_button.setStyleSheet("QPushButton {"
                          "     text-align: center;"
                          "     font-size: 14px;"
                          "}")

elixir_button = QPushButton("Elixir")
elixir_button.setIcon(elixir_icon)
elixir_button.setIconSize(QSize(20, 20))
elixir_button.setStyleSheet("QPushButton {"
                             "     text-align: center;"
                             "     font-size: 14px;"
                             "}")

trophy_drop_button = QPushButton("Trophy Drop")
trophy_drop_button.setIcon(diamond_icon)
trophy_drop_button.setIconSize(QSize(20, 20))
trophy_drop_button.setStyleSheet("QPushButton {"
                                 "     text-align: center;"
                                 "     font-size: 14px;"
                                 "}")

exit_button = QPushButton("Exit")

# Ajout des boutons au layout des boutons
button_layout.addWidget(gold_button)
button_layout.addWidget(elixir_button)
button_layout.addWidget(trophy_drop_button)

# Ajout des labels au layout des labels
gold_nb_boucles_label = QLabel("Gold loops number:")
elixir_nb_boucles_label = QLabel("Elixir loops number:")
elixir_nb_iterations_label = QLabel("Elixir iterations number:")
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

# Définition du layout principal pour la fenêtre
window.setLayout(main_layout)

# Connexion des boutons aux fonctions d'exécution
def execute_gold():
    nb_boucles = gold_nb_boucles_entry.text()
    print("Executing gold script with", nb_boucles, "loops")
    script_path = "../../gold_crash_100%.py"
    thread = ExecutionThread(script_path, nb_boucles)
    thread.execution_progress.connect(progress_bar.setValue)
    thread.start()

def execute_elixir():
    nb_boucles = elixir_nb_boucles_entry.text()
    nb_iterations = elixir_nb_iterations_entry.text()
    print("Executing elixir script with", nb_boucles, "loops and", nb_iterations, "iterations")
    script_path = "../../elixir.py"
    thread = ExecutionThread(script_path, nb_boucles, nb_iterations)
    thread.execution_progress.connect(progress_bar.setValue)
    thread.start()

def execute_trophy_drop():
    nb_boucles = trophy_drop_nb_boucles_entry.text()
    print("Executing trophy_drop script with", nb_boucles, "loops")
    script_path = "../../trophy_drop.py"
    thread = ExecutionThread(script_path, nb_boucles)
    thread.execution_progress.connect(progress_bar.setValue)
    thread.start()

gold_button.clicked.connect(execute_gold)
elixir_button.clicked.connect(execute_elixir)
trophy_drop_button.clicked.connect(execute_trophy_drop)

# Fonction de sortie de l'application
def exit_application():
    app.quit()

exit_button.clicked.connect(exit_application)

# Création de la barre de progression
progress_bar = QProgressBar()
progress_bar.setFixedSize(300, 20)
exit_layout.addWidget(progress_bar)
exit_layout.addWidget(exit_button)

# Ajout du layout de sortie au layout principal
main_layout.addLayout(exit_layout)

# Affichage de la fenêtre
window.show()

# Exécution de l'application PyQt
sys.exit(app.exec_())