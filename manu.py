from menu_items import main_manu
from patients import Patients, Appointments
from staff import Staff
from tasks import Tasks
from generators import Generator
from services import AllServices

#კლასი მთავარი მენიუ
class MainMenu:
    #კონსტრუქტორი
    def __init__(self):
        self.manu = main_manu
        self.registrattion_desk_menu = RegistrationDeskMenu()
        self.management_menu = ClinicManagementMenu()
        self.accounting_menu = ClinicAccountingMenu()
    
    #მენიუს ჩვენების ფუნქცია
    def display(self):
        for key, value in self.manu.items():
            print(f"{key}: {value}")
    
    #არჩევანის ფუნქცია
    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice
    
    def menu_select(self, choice):
        if choice == "1":
            self.registrattion_desk_menu.display()
        elif choice == "2":
            self.management_menu.display()
        elif choice == "3":
            self.accounting_menu.display()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")

#რეგისტრატორის მენიუ
class RegistrationDeskMenu:
    #კონსტრუქტორი
    def __init__(self):
        self.patient = Patients()
           
    def display(self):
        while True:
            print("1. Register new Patient: ") 
            print("2. Open/view medical history: ")                         
            print("3. Register appointment to doctor: ")                         
            print("4. Reaserch/Service: ")         
            print("5. Exit")

            choice = input("Please choose an option: ")
            if choice == "5":
                    break
            else:
                self.menu_select(choice)
    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def menu_select(self, choice):
        self.generate = Generator()
        self.services = AllServices()
        self.patients = Patients()
        self.appointments = Appointments()
        if choice == "1":
            id = str(input('Please enter patients ID number: ' ))
            uid = self.generate.generate_uid(id)
            name = str(input('Please enter patients name: '))
            surname =str(input('Please enter patients surname: '))
            date_of_birth = input('please enter date of birth (y-m-d): ')
            insurance_covarage = int(input('Please enter patients insurance covarage: '))
            patient_history = str(input('please enter information about patients diseas amd cpmplains: '))
            self.patient.register(uid, name,surname, date_of_birth, insurance_covarage, patient_history)
        elif choice == "2":
            self.patients.open_history()
        elif choice == "3":
            self.appointments.make_appointment()
        elif choice == "4":
            self.services.select_services()  
        elif choice == "6":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")

#მენეჯმენტის მენიუ

class ClinicManagementMenu:
    #კონსტრუქტორი
    def __init__(self):
        self.staff = Staff()       
    def display(self):
        while True:
            print("1. View full List of Staff: ") #პაციენტის რეგისტრაციია. უნდა შეგვაყვანინოს სახელი, გვარი, პირადი ნომერი, დაბადების წელი, ტელეფონის ნომერი, აგნერირებს უნიკალურ აიდის, შეინახოს ინფორმაცია ფაილში. 
            print("2. View List of support staff on duty: ") #იკითხოს რეგისტრირებულია თუ არა პაციენტი, თუ კი მოითხოვოს პირადი ნომერი და შემდეგ შეიყვანოს ანამნეზის მონაცემები. 
                                     #თუ არა გაიაროს რეგისტრაციის პროცესი და შემდეგ ანამნეზის მონაცემბები (ინფორმაცია შეინახოს სამედიცინო ისტორიის ფაილში)
            print("3. View List of doctors on duty: ")# გადაამისამართოს პაციენტი ექიმთან, პაციენტის მონაცემებს უნდა გაყვეს სამედიცინო ისტორია. 
                                      # ექიმის ქვე მენიუ - დაამატოს პაციენტის ისტორიას დანიშნულება. ეს ინფორმაცია ავტომატურად უნდა აისახის სამედიცინო ისტორიაში.
            print("4. View List of nuerses on duty: ")  #შეგვყავს პაციენტის პირადი ნომერი ან UID, გამოდის ქვე მენიუ სადაც ვირჩევთ თუ რა კვლევა უნდა ჩაუტარდეს პაციენტს, 
                           #პროგრამა გვეკითხება დავამატოთ თუ არა ერთის გარდა კიდევ სხვა კვლევა. შემდეგ იღებს მონაცემებს წინასწარ გამზადებული ბაზიდან. ანგარიშობს გადასახდელ თანხას 
                           #და ბეჭდავს ინფორმაციას. ამატებს პაციენტის ისტორიას კვლევების შესახებ მონაცემებს.
            print("5. Create task and asigne personal to it: ") #პირადი ნომრით ეძებს პაციენტის სამედიცინო ისტორიას და ბეჭდავს სრულ მონაცემებს.
            print("6. Add new staff memeber: ") #პირადი ნომრით ეძებს მხოლოდ ინფორმაციას კველების შესახებ და ბეჭდავს.
            print("7. Remove staff memeber: ") # პაციენტს ჩაწერს ექიმთან, სმს-ის სახით გაუგზავნის ინფორმაციას პაციენტს
        
            print("8. Exit")


            choice = input("Please choose an option: ")
            if choice == "8":
                break
            else:
                self.menu_select(choice)

    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def menu_select(self, choice):
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
            id = input('Please enter ID number: ' )        
            name = str(input('Please enter name: ').lower())
            surname =str(input('Please enter  surname: ').lower())
            position = input('Please enter position: ').lower()
            salary= float(input('please enter salary: '))
            status= input('please enter status (on duty/ not on duty): ').lower()
            assigned_task = input('please enter what task do you give to this person: ')
            self.staff.add_staff_member(id,name,surname,position,salary, status,assigned_task)
        elif choice == "7":
            Staff.remove_staff_member()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")        


#ბუღალტერის მენიუ


class ClinicAccountingMenu:
            
    def display(self):
        while True:
            print("1. Calculate cost of the procedure: ") #პაციენტის რეგისტრაციია. უნდა შეგვაყვანინოს სახელი, გვარი, პირადი ნომერი, დაბადების წელი, ტელეფონის ნომერი, აგნერირებს უნიკალურ აიდის, შეინახოს ინფორმაცია ფაილში. 
            print("2. Calculate salary for staff member: ") #იკითხოს რეგისტრირებულია თუ არა პაციენტი, თუ კი მოითხოვოს პირადი ნომერი და შემდეგ შეიყვანოს ანამნეზის მონაცემები. 
                                     #თუ არა გაიაროს რეგისტრაციის პროცესი და შემდეგ ანამნეზის მონაცემბები (ინფორმაცია შეინახოს სამედიცინო ისტორიის ფაილში)
            print("3. View services that hospital is providing: ")# გადაამისამართოს პაციენტი ექიმთან, პაციენტის მონაცემებს უნდა გაყვეს სამედიცინო ისტორია. 
                                      # ექიმის ქვე მენიუ - დაამატოს პაციენტის ისტორიას დანიშნულება. ეს ინფორმაცია ავტომატურად უნდა აისახის სამედიცინო ისტორიაში.
            print("4. View last monthes income: ")  #შეგვყავს პაციენტის პირადი ნომერი ან UID, გამოდის ქვე მენიუ სადაც ვირჩევთ თუ რა კვლევა უნდა ჩაუტარდეს პაციენტს, 
                           #პროგრამა გვეკითხება დავამატოთ თუ არა ერთის გარდა კიდევ სხვა კვლევა. შემდეგ იღებს მონაცემებს წინასწარ გამზადებული ბაზიდან. ანგარიშობს გადასახდელ თანხას 
                           #და ბეჭდავს ინფორმაციას. ამატებს პაციენტის ისტორიას კვლევების შესახებ მონაცემებს.
                  
            print("5. Exit")


            choice = input("Please choose an option: ")
            if choice == "5":
                break
            else:
                self.menu_select(choice)

    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def menu_select(self, choice):
        if choice == "1":
            pass
            #Services.calculate_total_cost()
        elif choice == "2":
            pass
            #Salaries.calculate_salary()
        elif choice == "3":
            pass
            #Services.view_all_services()
        elif choice == "4":
           pass
            #Services.calculate_income()
        elif choice == "5":
            
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")

#დავალებების მენიუ


class TasksSubMenu:
           
    def display(self):
        for key, value in self.menu.items():
            print(f"{key}: {value}")
    def get_user_choice(self):
        choice = input("Please choose an option: ")
        return choice

    def menu_select(self, choice):
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
"""
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
            AllServices.selec_services()
        elif choice == "2":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice, please try again.")
#მენეჯმენტის მენიუ
"""           