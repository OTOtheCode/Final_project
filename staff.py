import os
import pandas as pd

staff_columns = ['ID', 'Name', 'Surname', 'Position', 'salary', 'status', 'Assigned_task', ]

class Staff:
    def __init__(self):
        pass
    def add_staff_member(self,id,name,surname,position,salary, status,assigned_task):
        self.id = id
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
        
        # Convert the patient data dictionary to a DataFrame
        
        staff_df = pd.DataFrame([staff_data])
        
        # Concatenate the existing DataFrame with the new patient DataFrame
        combined_df = pd.concat([existing_df, staff_df], ignore_index=True)
        
        # Save the updated DataFrame back to the CSV file
        combined_df.to_csv(file_path, sep=';', index=False,)
        print(f"{position} {name} {surname} registered successfully.")
    def remove_staff_member():
        pass
    def view_all_staff_members():
        pass
    def view_doctors_on_duty ():
        pass
    def view_support_staff_on_duty():
        pass
    def View_nurses_on_Duty():
        pass
    
class Salaries:
    def __init__(self):
        pass
    def calculate_salary():
        pass
