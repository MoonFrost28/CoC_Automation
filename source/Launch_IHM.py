import sys
import subprocess
import Interface_variables
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QSpacerItem 
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

# Initialisation of interface variables
text_width = Interface_variables.text_width
text_height = Interface_variables.text_height 
image_width = Interface_variables.image_width
image_height = Interface_variables.image_height
entry_width = Interface_variables.entry_width
button_height = Interface_variables.button_height
button_width = Interface_variables.button_width

# Définition des fonctions
def execute_gold():
    nb_loops = gold_nb_loops_entry.text()
    if nb_loops=="":
        nb_loops = str(1)
    script_path = "source/gold_crash_100%.py"
    subprocess.run(["pythonw", script_path, nb_loops])

def execute_elixir():
    nb_loops = elixir_nb_loops_entry.text()
    nb_iterations = elixir_nb_iterations_entry.text()
    if nb_loops=="":
        nb_loops = str(1)
    if nb_iterations=="":
        nb_iterations = str(1)      
    script_path = "source/elixir.py"
    subprocess.run(["pythonw", script_path, nb_loops, nb_iterations])

def execute_trophy_drop():
    nb_loops = trophy_drop_nb_loops_entry.text()
    if nb_loops=="":
        nb_loops = str(1)
    script_path = "source/trophy_drop.py"
    subprocess.run(["pythonw", script_path, nb_loops])

def exit_application():
    app.quit()

def pause_gold():
    print ("TO DO")

def pause_elixir():
    print ("TO DO")

def pause_trophy_drop():
    print ("TO DO")

# Création de l'application PyQt
app = QApplication(sys.argv)

# Création de la fenêtre principale
window = QWidget()
window.setWindowTitle("Clash of Clans script")
app.setWindowIcon(QIcon("Images/CoC_icon.ico"))

# Création des layouts pour organiser les éléments
main_layout = QGridLayout()

gold_layout = QVBoxLayout()
elixir_layout = QVBoxLayout()
trophy_drop_layout = QVBoxLayout()
bottom_layout = QHBoxLayout()

gold_text_layout = QHBoxLayout()
elixir_text_layout = QHBoxLayout()
trophy_drop_text_layout = QHBoxLayout()

gold_entry_layout = QHBoxLayout()
elixir_entry_layout = QGridLayout()
trophy_drop_entry_layout = QHBoxLayout()

gold_checkbox_layout = QHBoxLayout()
trophy_drop_checkbox_layout = QHBoxLayout()

gold_button_layout = QHBoxLayout()
elixir_button_layout = QHBoxLayout()
trophy_drop_button_layout = QHBoxLayout()

# Création des icônes à partir des fichiers d'images
gold_pixmap = QPixmap("Images/GoldB.png")
gold_icon = QIcon(gold_pixmap)

elixir_pixmap = QPixmap("Images/ElixirB.png")
elixir_icon = QIcon(elixir_pixmap)

diamond_pixmap = QPixmap("Images/Diamond_LeagueB.png")
diamond_icon = QIcon(diamond_pixmap)

icon = QIcon("Images/CoC_icon.ico")

# Création des labels des scripts
gold_image = QLabel()
gold_image.setPixmap(QPixmap("Images/GoldB.ico"))
gold_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
gold_image.setStyleSheet("""
    background-color: antiquewhite;
    border-left: 2px solid brown;
    border-top: 2px solid brown;
    border-bottom: 2px solid brown;
    padding: 10px 0px 10px 10px;
    """)
gold_image.setFixedSize(image_width, image_height)

gold_label = QLabel("Gold farming")
gold_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
gold_label.setStyleSheet("""
    background-color: antiquewhite;
    color: gray;
    border-right: 2px solid brown;
    border-top: 2px solid brown;
    border-bottom: 2px solid brown;
    font-weight: bold;
    padding: 10px 10px 10px 10px;
    """)
gold_label.setFixedSize(text_width, text_height)

gold_text_layout.addWidget(gold_image)
gold_text_layout.addWidget(gold_label)
gold_text_layout.setSpacing(0)

elixir_image = QLabel()
elixir_image.setPixmap(QPixmap("Images/ElixirB.ico"))
elixir_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
elixir_image.setStyleSheet("""
    background-color: antiquewhite;
    border-left: 2px solid brown;
    border-top: 2px solid brown;
    border-bottom: 2px solid brown;
    padding: 10px 0px 10px 10px;
    """)
elixir_image.setFixedSize(image_width, image_height)

elixir_label = QLabel("Elixir farming")
elixir_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
elixir_label.setStyleSheet("""
    background-color: antiquewhite;
    color: gray;
    border-right: 2px solid brown;
    border-top: 2px solid brown;
    border-bottom: 2px solid brown;
    font-weight: bold;
    padding: 10px 10px 10px 10px;
    """)
elixir_label.setFixedSize(text_width, text_height)

elixir_text_layout.addWidget(elixir_image)
elixir_text_layout.addWidget(elixir_label)
elixir_text_layout.setSpacing(0)

trophy_drop_image = QLabel()
trophy_drop_image.setPixmap(QPixmap("Images/Diamond_LeagueB.ico"))
trophy_drop_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
trophy_drop_image.setStyleSheet("""
    background-color: antiquewhite;
    border-left: 2px solid brown;
    border-top: 2px solid brown;
    border-bottom: 2px solid brown;
    padding: 10px 0px 10px 10px;
    """)
trophy_drop_image.setFixedSize(image_width, image_height)

trophy_drop_label = QLabel("Trophy drop")
trophy_drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
trophy_drop_label.setStyleSheet("""
    background-color: antiquewhite;
    color: gray;
    border-right: 2px solid brown;
    border-top: 2px solid brown;
    border-bottom: 2px solid brown;
    font-weight: bold;
    padding: 10px 10px 10px 10px;
    """)
trophy_drop_label.setFixedSize(text_width, text_height)

trophy_drop_text_layout.addWidget(trophy_drop_image)
trophy_drop_text_layout.addWidget(trophy_drop_label)
trophy_drop_text_layout.setSpacing(0)

# Création des boutons
gold_play_button = QPushButton("Play")
gold_play_button.clicked.connect(execute_gold)
gold_play_button.setFixedSize(button_width, button_height)
gold_pause_button =QPushButton("Pause")
gold_pause_button.clicked.connect(pause_gold)
gold_pause_button.setFixedSize(button_width, button_height)

gold_button_layout.addWidget(gold_play_button)
gold_button_layout.addWidget(gold_pause_button)
gold_button_layout.setSpacing(0)

elixir_play_button = QPushButton("Play")
elixir_play_button.clicked.connect(execute_elixir)
elixir_pause_button = QPushButton("Pause")
elixir_pause_button.clicked.connect(pause_elixir)

elixir_button_layout.addWidget(elixir_play_button)
elixir_button_layout.addWidget(elixir_pause_button)
elixir_button_layout.setSpacing(0)

trophy_drop_play_button = QPushButton("Play")
trophy_drop_play_button.clicked.connect(execute_trophy_drop)
trophy_drop_pause_button = QPushButton("Pause")
trophy_drop_pause_button.clicked.connect(pause_trophy_drop)

trophy_drop_button_layout.addWidget(trophy_drop_play_button)
trophy_drop_button_layout.addWidget(trophy_drop_pause_button)
trophy_drop_button_layout.setSpacing(0)

exit_button = QPushButton("Exit")
exit_button.clicked.connect(exit_application)

gold_checkbox = QCheckBox("Collect elixir")
gold_checkbox.setChecked(True)

gold_checkbox_layout.addStretch()
gold_checkbox_layout.addWidget(gold_checkbox)
gold_checkbox_layout.addStretch()

trophy_drop_checkbox = QCheckBox("Collect elixir")
trophy_drop_checkbox.setChecked(True)

trophy_drop_checkbox_layout.addStretch()
trophy_drop_checkbox_layout.addWidget(trophy_drop_checkbox)
trophy_drop_checkbox_layout.addStretch()

# Création des zones d'entrée
gold_nb_loops_label = QLabel("Loops number:")
gold_nb_loops_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
gold_nb_loops_entry = QLineEdit()
gold_nb_loops_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
gold_nb_loops_entry.setFixedWidth(entry_width)

gold_entry_layout.addWidget(gold_nb_loops_label)
gold_entry_layout.addWidget(gold_nb_loops_entry)

elixir_nb_loops_label = QLabel("Loops number:")
elixir_nb_loops_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
elixir_nb_loops_entry = QLineEdit()
elixir_nb_loops_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
elixir_nb_loops_entry.setFixedWidth(entry_width)

elixir_nb_iterations_label = QLabel("Iterations number:")
elixir_nb_iterations_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
elixir_nb_iterations_entry = QLineEdit()
elixir_nb_iterations_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
elixir_nb_iterations_entry.setFixedWidth(entry_width)

elixir_entry_layout.addWidget(elixir_nb_loops_label, 0, 0)
elixir_entry_layout.addWidget(elixir_nb_loops_entry, 0, 1)
elixir_entry_layout.addWidget(elixir_nb_iterations_label, 1, 0)
elixir_entry_layout.addWidget(elixir_nb_iterations_entry, 1, 1)

trophy_drop_nb_loops_label = QLabel("Loops number:")
trophy_drop_nb_loops_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
trophy_drop_nb_loops_entry = QLineEdit()
trophy_drop_nb_loops_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
trophy_drop_nb_loops_entry.setFixedWidth(entry_width)

trophy_drop_entry_layout.addWidget(trophy_drop_nb_loops_label)
trophy_drop_entry_layout.addWidget(trophy_drop_nb_loops_entry)

# Ajout des boutons au layout
# Gold layout
gold_layout.addLayout(gold_text_layout)
gold_layout.addLayout(gold_entry_layout)
gold_layout.addStretch()
gold_layout.addLayout(gold_checkbox_layout)
gold_layout.addLayout(gold_button_layout)

# Elixir layout
elixir_layout.addLayout(elixir_text_layout)
elixir_layout.addLayout(elixir_entry_layout)
elixir_layout.addLayout(elixir_button_layout)

# Trophy drop layout
trophy_drop_layout.addLayout(trophy_drop_text_layout)
trophy_drop_layout.addLayout(trophy_drop_entry_layout)
trophy_drop_layout.addStretch()
trophy_drop_layout.addLayout(trophy_drop_checkbox_layout)
trophy_drop_layout.addLayout(trophy_drop_button_layout)

main_layout.addLayout(gold_layout, 0, 0)
main_layout.addLayout(elixir_layout, 0, 1)
main_layout.addLayout(trophy_drop_layout, 0, 2)
main_layout.addWidget(exit_button, 1, 2)

# Définition du layout principal pour la fenêtre
window.setLayout(main_layout)

# Affichage de la fenêtre
window.show()

# Exécution de l'application PyQt
sys.exit(app.exec_())
