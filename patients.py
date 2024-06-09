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
#პაციენტის კლასი
class Patients:
    
    def __init__(self):
       pass 
    
    #ასაკის დაანგარეიშების ფუნქცია
    def calculate_age (self, date_of_birth):
        today = datetime.today()
        disp = datetime.strptime(date_of_birth, "%Y-%m-%d")
        return today.year - disp.year - ((today.month, today.day)<(disp.month,disp.day))
    
    #პაციენტის რეგისტრაციის ფუნქცია
    def register (self,id,name,surname,date_of_birth,insurance_covarage, patient_history):
        #ვსაზღვრავთ მონაცემებს
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
        #ვამოწმებთ ცარიელი არის თუ არა ფაილი, თუ ცარიელი ვბეჭდავთ კოლონის სათაურებს ჯერ. თუ არა ვტოვებთ და მხოლოდ პაციენტის მონაცემებს ვამატებთ
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            existing_df = pd.read_csv(file_path, sep=';')
        else:
            existing_df = pd.DataFrame(columns=patient_columns)
        
        #გადაგვაქვს პაციენტის მონაცემები დატაფრეიმში  და ვაკეთებთ არსებულის და ახალი დატაფრემის კონკანაციას.  
        patient_df = pd.DataFrame([patient_data])
        combined_df = pd.concat([existing_df, patient_df], ignore_index=True)
        
        #ვინახავთ ფაილში
        combined_df.to_csv(file_path, sep=';', index=False,)
        print(f"Patient {name} {surname} registered successfully.")   

    def open_history ():
        pass
           
    def add_to_doctor ():
        pass
    def view_hist():
        pass
    def view_research():
        pass
    def appointment():
        pass
    