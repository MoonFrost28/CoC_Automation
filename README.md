# CoC_Automation
Python scripts for automating resources gathering in builder base.

# Usage
1. Install [Python](https://www.python.org/downloads/) and install the following modules using [**pip install**](https://pypi.org/project/pip/) :
    - **pyinstaller**
    - **pyautogui**
    - **pynput**
    - **PyQt5**
    - **importlib**
    - **Pillow**

2. Download project
4. Import keyconfig file (*com.supercell.clashofclans.cfg*) to your Bluestacks profile, if needed, please check link [Import control scheme](https://support.bluestacks.com/hc/en-us/articles/360056129291-How-to-import-your-game-controls-from-BlueStacks-4-and-use-them-in-BlueStacks-5#:~:text=After%20the%20game%20launches%2C%20open,on%20the%20%22Import%22%20icon.). 
5. Run IHM, by launching the .exe file.
6. Enter a number and run selected script by pressing the correct button according to the script you want to run. More detail below.

# Roadmap
- [x] Factorize codes to be more modular
- [x] Add interface and .exe file for easier use
- [ ] Add trophy calculation for optimized farming
- [ ] Add tick icon to activate elixir collection or not in gold macro
- [ ] Add pause button
- [ ] Redo script interface with different buttons for execution and presentation
- [ ] Update script with background activated inputs

# Strategy

The goal is to drop around ~2000 trophies to be strong enough and ensure strong wins against opponents as well as strong defenses. Opponents will not be strong enough to destroy your village.

# File description

All source files are in the source folder.
The only files you will potentially use are the one described below.

## elixir.py

Farm builer elixir by dropping hero and instantly surrendering.
Being low enough in trophies allow you to have great defenses against opponent and thus, winning elixir.  

This file uses the [*farm_elixir()*](README.md#farm_elixir) and the [*collect_elixir_cart()*](README.md#collect_elixir_cart) functions.

## get_mouse_pos.py

Get mouse coordinates when clicking on the mouse. Needed for the [*quit_game()*](README.md#quit_game) function.
Use it once to get coordinates for the two clicks the script needs to perform.
1. On the homescreen of Bluestacks, click on the Clash of Clans icon to get the coordinates of the icon, note them. (TIP: press Windows key to get the coordinates in your terminal, otherwise it will just launch the game)
2. Same process with the "CLOSE ALL" button on the Recent Apps menu.
Coordinates don't need to be exact but make sur they are in the zone of the button. 

## gold_crash_100%

Farm builer gold by dropping hero and troups, activating their power, then quitting the game and restarting it.
There's a mechanic in the game that allows you to close the game and finish the ongoing attack instantly, without waiting for the troops to destroy the village.
Timings to get 200% is quite hard, therefore the script focuses on running attacks on the first village only. [^1]  

This file uses the [*farm_gold()*](README.md#farm_gold), the [*quit_game()*](README.md#quit_game) and the [*collect_elixir_cart()*](README.md#collect_elixir_cart) functions.

[^1]: In case you are low enough, there is only one village available in the builder base.

## keys_config.py

This file is used as a config file to link between the controls config in Bluestacks and the key simulated using the script. Using the config file provided with the project should work as it is.
If you are using your own config file, please make sure this *keys_config.py* file is coherent with config file from BlueStacks.

## trophy_drop.py

This script allows you to drop in trophies in case you feel you are too high to make the other scripts work. It functions in the same way the elixir script works beside that it uses an "open" village in order for you to lose defenses. 
Before running the script, it changes village to put an other village that you will have dedicated to lose trophies.[^2]  

***PLEASE***, before running the script, make sure no trees or oher elements of decoration are in the way of the new village, otherwise it will not work. This script is to be used preferentially after cleaning your village.  

This file uses the [*change_village()*](README.md#change_village), the [*reset_village()*](README.md#reset_village), the [*farm_elixir()*](README.md#farm_elixir) and the [*collect_elixir_cart()*](README.md#collect_elixir_cart) functions.

[^2]: It can be your village where you display your remaining upgrades with all defenses on one side for example.

## functions.py

File with the definition and the algorithm behind the various scripts. See below for more details about each function.

## Launch_IHM.py

File to describe the user interface, no need to be modified.

# Function description and how to use them

## collect_elixir_cart()

This function performs a sequence of keys to collect elixir from elixir cart.
It uses 2 parameters with one being set as a default value. The first parameter is only used if the temporisation is activated *activate_temporisation = True*.

## farm_elixir()

This function performs a sequence of keys to drop the hero then surrendering immediately after.

## farm_gold()

This function performs a sequence of keys to drop the hero and all the troops, it uses their capacity as well.

## change_village()

This function performs a sequence of keys to change from your default village to an "open" village before the script [*trophy_drop.py*](README.md#trophy_droppy) is started.  
Please make sure to update [*keys_config.py*](README.md#keys_configpy) with the position of your villages. Using the Bluestacks config file provided, here are the default keys:
- q: for left village
- s: for center village
- d: for right village

## reset_village()

This function performs a sequence of keys to change from your "open" village to your default village after the script [*trophy_drop.py*](README.md#trophy_droppy) is terminated.  
Please make sure to update [*keys_config.py*](README.md#keys_configpy) with the position of your villages. Using the Bluestacks config file provided, here are the default keys:
- q: for left village
- s: for center village
- d: for right village

## quit_game()

This function performs a sequence of keys to close the game and restart it.
***PLEASE*** make sure the coordinates used in this function match with the coordinates of your interface.
