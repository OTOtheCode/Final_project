from menu_items import main_manu
from manu import MainMenu

if __name__ == "__main__":
    

    menu = MainMenu(main_manu)
    while True:
        MainMenu.display(menu)
        choice = MainMenu.choice(menu)
        if choice.lower() == "x":
            break
        MainMenu.user_choice(main_manu, choice)