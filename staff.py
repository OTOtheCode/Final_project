import os
import pandas as pd
from generators import Generator
staff_columns = ['ID', 'Name', 'Surname', 'Position', 'salary', 'status', 'Assigned_task', ]

#თანამშრომლების კლასი
class Staff:
    def __init__(self):
        pass
    #თანამშრომლის დამატება
    def add_staff_member(self,id,name,surname,position,salary, status,assigned_task):
        self.generator = Generator()
        self.id = self.generator.generate_uid(id)
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.status = status
        self.assigned_task = assigned_task
        
        staff_data = {
            'ID':self.id,
            'Name': self.name,
            'Surname': self.surname,
            'Position': self.position,
            'salary': self.salary,
            'status' : self.status,
            'Assigned_task': self.assigned_task
        }
        
        file_path = 'staff.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            existing_df = pd.read_csv(file_path, sep=';')
        else:
            existing_df = pd.DataFrame(columns=staff_columns)
             
        staff_df = pd.DataFrame([staff_data])
        
        combined_df = pd.concat([existing_df, staff_df], ignore_index=True)
                
        combined_df.to_csv(file_path, sep=';', index=False,)
        print(f"{position} {name} {surname} registered successfully.")
    
    #თანამშრომლის წაშლა
    def remove_staff_member(self):
        self.generator = Generator()
        file_path = 'staff.csv'
        id = input('Please enter staff memeber ID: ')
        uid = self.generator.generate_uid(id)
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            existing_df = pd.read_csv(file_path, sep=';')
            if uid in existing_df['ID'].values:
                updated_df = existing_df[existing_df['ID'] != uid]
                updated_df.to_csv(file_path, sep=';', index=False)
                print(f"Staff member with ID {id} removed successfully.")
            else:
                print(f"Staff member with ID {id} not found.")
        else:
            print("Staff file does not exist or is empty.")
    
    #თანამშრომლების სიის გამოტანა პოზიციების მიხედვით
    def print_staff_by_position(self, position):
        file_path = 'staff.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            df = pd.read_csv(file_path, sep=';')
            position_df = df[df['Position'] == position]
            print(f"All {position}s:")
            print(position_df)
        else:
            print("Staff file does not exist or is empty.")

    #ყველა თანამშრომლის სიის გამოტანა
    def print_all_staff(self):
        file_path = 'staff.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            df = pd.read_csv(file_path, sep=';')
            print("All Staff Members:")
            print(df)
        else:
            print("Staff file does not exist or is empty.")
    
    #მხოლოდ ექიმების გამოტანა
    def print_all_doctors(self):
        self.print_staff_by_position('doctor')
    
    #მხოლოდ ექთნების გამოტანა
    def print_all_nurses(self):
        self.print_staff_by_position('nurse')
    
    #მორიგეების გამოტანა
    def print_on_duty_staff(self):
        file_path = 'staff.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            df = pd.read_csv(file_path, sep=';')
            on_duty_df = df[df['status'] == 'on duty']
            print("On Duty Staff Members (Name, Surname, Position):")
            print(on_duty_df[['Name', 'Surname', 'Position']])
        else:
            print("Staff file does not exist or is empty.")
            
