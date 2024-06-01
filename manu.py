from menu_items import main_manu, MENU_clinic_accounting, MENU_clinic_mangment, MENU_registration_desk, SUB_menu_doctor, SUB_menu_tasks, SUB_menu_researches
from patients import Patient
from services import Researches, Services
from staff import Staff, Salaries
from tasks import Tasks
#მთავარი მენიუ

class MainMenu:
    def __init__(self):
        self.manu = main_manu
        
    def display(self):
        for key, value in self.manu.items():
            print(f"{key}: {value}")
    
    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def handle_choice(self, choice):
        if choice == "1":
            RegistrationDeskMenu.display()
        elif choice == "2":
            ClinicManagementMenu.display()
        elif choice == "3":
            ClinicAccountingMenu.display()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")
#რეგისტრატორის მენიუ

class RegistrationDeskMenu:
    def __init__(self):
        self.menu = MENU_registration_desk
        
    def display(self):
        for key, value in self.menu.items():
            print(f"{key}: {value}")
    
    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def handle_choice(self, choice):
        if choice == "1":
            Patient.register()
        elif choice == "2":
            Patient.open_history()
        elif choice == "3":
            Patient.add_to_doctor()
        elif choice == "4":
            ResearchesMenu.display()
        elif choice == "5":
            Patient.view_hist()
        elif choice == "6":
            Patient.view_research()
        elif choice == "7":
            Patient.appointment()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")


"""
#ექიმის მენიუ

class DoctorMenu:
    def __init__(self):
        self.menu = SUB_menu_doctor
        
    def display(self):
        for key, value in self.menu.items():
            print(f"{key}: {value}")
"""
#კვლევების მენიუ

class ResearchesMenu:
    def __init__(self):
        self.menu = SUB_menu_researches
        
    def display(self):
        for key, value in self.menu.items():
            print(f"{key}: {value}")
    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def handle_choice(self, choice):
        if choice == "1":
            Researches.add_research_1()
        elif choice == "2":
            Researches.add_research_2()
        elif choice == "3":
            Researches.add_research_3()
        elif choice == "4":
            Researches.add_research_4()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")
#მენეჯმენტის მენიუ

class ClinicManagementMenu:
    def __init__(self):
        self.menu = MENU_clinic_mangment
        
    def display(self):
        for key, value in self.menu.items():
            print(f"{key}: {value}")

    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def handle_choice(self, choice):
        if choice == "1":
            Staff.view_all_staff_members()
        elif choice == "2":
            Staff.view_support_staff_on_duty()
        elif choice == "3":
            Staff.view_all_staff_members()
        elif choice == "4":
            Staff.View_nurses_on_Duty()
        elif choice == "5":
            TasksSubMenu.display()
        elif choice == "6":
            Staff.add_staff_member()
        elif choice == "7":
            Staff.remove_staff_member()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")        

#დავალებების მენიუ


class TasksSubMenu:
    def __init__(self):
        self.menu = SUB_menu_tasks
        
    def display(self):
        for key, value in self.menu.items():
            print(f"{key}: {value}")
    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def handle_choice(self, choice):
        if choice == "1":
            Tasks.create_task()
        elif choice == "2":
            Tasks.remove_task()
        elif choice == "3":
            Tasks.view_all_tasks()
        elif choice == "4":
            Tasks.view_persons_tasks()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")
#ბუღალტერის მენიუ
class ClinicAccountingMenu:
    def __init__(self):
        self.menu = MENU_clinic_accounting
        
    def display(self):
        for key, value in self.menu.items():
            print(f"{key}: {value}")
    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def handle_choice(self, choice):
        if choice == "1":
            Services.calculate_total_cost()
        elif choice == "2":
            Salaries.calculate_salary()
        elif choice == "3":
            Services.view_all_services()
        elif choice == "4":
            Services.calculate_income()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")