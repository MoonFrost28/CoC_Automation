# CoC_Automation
Python scripts for automating resources gathering in builder base.

# Usage
1. Install Python[https://www.python.org/downloads/] and following modules :
    - **pyautogui**
    - **importlib**

2. Download project
3. Import keyconfig file (*com.supercell.clashofclans.cfg*) to your Bluestacks profile, if needed, please check link [Import control scheme](https://support.bluestacks.com/hc/en-us/articles/360056129291-How-to-import-your-game-controls-from-BlueStacks-4-and-use-them-in-BlueStacks-5#:~:text=After%20the%20game%20launches%2C%20open,on%20the%20%22Import%22%20icon.). 
4. Personnalize profile as you wish and adapt profile in `keys_config.py` file
5. Launch IHM, enter a number and run selected script by pressing the button

# Roadmap
- [x] Factorize codes to be more modular
- [x] Add interface and .exe file for easier use
- [ ] Add trophy calculation for optimized farming
- [ ] Add tick icon to activate elixir collection or not in gold macro
- [ ] Add pause button
- [ ] Redo script interface with different buttons for execution and presentation
- [ ] Update script with background activated inputs

# Strategy

The goal is to drop around ~2000 trophies to be strong enough and ensure strong wins against opponents as well as strong defenses. Opponents will not be strong enough to destroy your village

# File description

## elixir.py

Farm builer elixir by dropping hero and instantly surrendering. 

## get_mouse_pos.py

## gold_crash_100%.

Drop all troups, close the game and restart it.

## keys_config.py

Keys sequence for various scripts.

## trophy_drop.py

Similar to elixir script but your builder village is set to lose defenses to drop trophies

## variables.py

File with the definition and the algorithm behind the scripts
