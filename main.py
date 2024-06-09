from menu_items import main_manu
from manu import MainMenu

def main():
    main_menu = MainMenu()  # Instantiate the MainMenu class
    while True:
        main_menu.display()  # Display the main menu
        choice = main_menu.get_user_choice()  # Get the user's choice
        main_menu.menu_select(choice)  # Handle the user's choice
       
        if choice == "4":
            break

if __name__ == "__main__":
    main()
