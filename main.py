from menu_items import main_manu
from manu import MainMenu
#მთავარი მენიუს გამშვები
def main():
    main_menu = MainMenu()  
    while True:
        main_menu.display()  
        choice = main_menu.get_user_choice()  
        main_menu.menu_select(choice)  
       
        if choice == "4":
            break

if __name__ == "__main__":
    main()
