import pandas as pd
import os
from patients import patient_columns
from staff import staff_columns


#ვალიდატორის კლასი
class Validator:
    
    def __init__(self):
        self.columns = patient_columns  

    #პაციენტი არის თუ არა უკვე ბაზაში
    def validate_patient (self, id):
        file_path = 'patients.csv'
        
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                existing_df = pd.read_csv(file_path, sep=';')
                if str(id) in existing_df['ID'].astype(str).values:
                    print(f"Patient with ID {id} already exists.")
                    return
                else:
                    existing_df = pd.DataFrame(columns=self.columns)