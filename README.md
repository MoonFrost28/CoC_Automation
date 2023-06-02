# CoC_Automation
Python scripts for automating resources gathering in builder base.

# Usage
1. Install python and following modules :
    - **pyautogui**
    - **importlib**

2. Download project
3. Import keyconfig file (*com.supercell.clashofclans.cfg*) to your Bluestacks profile, if needed, please check link [Import control scheme](https://support.bluestacks.com/hc/en-us/articles/360056129291-How-to-import-your-game-controls-from-BlueStacks-4-and-use-them-in-BlueStacks-5#:~:text=After%20the%20game%20launches%2C%20open,on%20the%20%22Import%22%20icon.). 
4. Personnalize profile as you wish and adapt profile in `keys_config.py` file
5. Run desired script by launching one of the following files :
    - `elixir.py`
    - `gold_crash_100%.py`
    - `trophy_drop.py`
6. For each file, a default of 1 loop is coded, however if more loops are needed, simply add the number of loops at the end of the line :
    - e.g. : `python gold_crash_100%.py 10`
    - Special conditions for `elixir.py` as it requires two arguments

# Roadmap
- [x] Factorize codes to be more modular
- [ ] Add interface and .exe file for easier use
- [ ] Add trophy calculation for optimized farming

# Strategy

The goal is to drop around ~2000 trophies to be strong enough and ensure strong wins against opponents as well as strong defenses. Opponents will not be strong enough to destroy your village

# File description

## elixir.py

Farm builer elixir by dropping hero and instantly surrendering. 

## get_mouse_pos.py

## gold_crash_100%.py

## keys_config.py

## trophy_drop.py

## variables.py
