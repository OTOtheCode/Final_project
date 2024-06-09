import pandas as pd
from datetime import datetime

import os
patient_columns = [
    'ID', 
    'Name', 
    'Surname', 
    'Date of Birth', 
    'Age', 
    'Insurance covarage', 
    'history']

class Patients:
    
    def __init__(self):
       pass #self.check_file = Validator()
    
    def calculate_age (self, date_of_birth):
        today = datetime.today()
        disp = datetime.strptime(date_of_birth, "%Y-%m-%d")
        return today.year - disp.year - ((today.month, today.day)<(disp.month,disp.day))
    
    def register (self,id,name,surname,date_of_birth,insurance_covarage, patient_history):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth = date_of_birth
        self.age = self.calculate_age(date_of_birth)
        self.insurance = insurance_covarage
        self.history = patient_history
        
        patient_data = {
            'ID':self.id,
            'Name': self.name,
            'Surname': self.surname,
            'Date of Birth': self.birth,
            'Age': self.age,
            'Insurance covarage' : self.insurance,
            'history': self.history
        }
        file_path = 'patients.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            existing_df = pd.read_csv(file_path, sep=';')
        else:
            existing_df = pd.DataFrame(columns=patient_columns)
        
        # Convert the patient data dictionary to a DataFrame
        
        patient_df = pd.DataFrame([patient_data])
        
        # Concatenate the existing DataFrame with the new patient DataFrame
        combined_df = pd.concat([existing_df, patient_df], ignore_index=True)
        
        # Save the updated DataFrame back to the CSV file
        combined_df.to_csv(file_path, sep=';', index=False,)
        print(f"Patient {name} {surname} registered successfully.")   

    def open_history ():
        pass
            #patient_df = pd.read_csv(patients)
    def add_to_doctor ():
        pass
    def view_hist():
        pass
    def view_research():
        pass
    def appointment():
        pass
    