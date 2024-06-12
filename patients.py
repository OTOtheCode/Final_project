import pandas as pd
from datetime import datetime
import os
from generators import Generator
#from validators import Validator
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
       #self.validator = Validator()
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
    
    #მხოლოდ პაციენტის ისტორიის მოდული
    def open_history (self):
        patient_id = input("Please enter the patient's ID: ").strip()
        uid = 'a' + patient_id
        self.file_path = 'patients.csv'
        patients_df = pd.read_csv(self.file_path, delimiter=';')
        
        if uid not in patients_df['ID'].astype(str).str.strip().values:
            print("Patient ID not found.")
            return
        
        patient_history = patients_df.loc[patients_df['ID'].astype(str).str.strip() == uid, 'history'].iloc[0]
        print(f"\nHistory for patient ID {uid}:")
        print(patient_history)


class Appointments:
    def __init__(self):
        self.staff_file = 'staff.csv'
        self.patients_file = 'patients.csv'
        self.appointments_file = 'appointments.csv'

    def make_appointment(self):
        #ვიღებთ თანამშრომლების მონაცემებს
        staff_df = pd.read_csv(self.staff_file, delimiter=';')

        # ცამოწმებთ თუ რომელი ექიმია მორიგე
        available_doctors = staff_df[(staff_df['Position'] == 'doctor') & (staff_df['status'] == 'on duty')]

        if available_doctors.empty:
            print("No doctors are currently on duty.")
            return

        # გამოგვყავს ეკრანზე მორიგე ექიმმები
        print("Available doctors on duty:")
        for idx, row in available_doctors.iterrows():
            print(f"{idx + 1}: Dr. {row['Name']} {row['Surname']}")

        # ვირჩევთ თ ვისთან ვწერთ პაციენტს
        while True:
            try:
                doctor_choice = int(input("Select a doctor by number: ")) - 1
                if doctor_choice < 0 or doctor_choice >= len(available_doctors):
                    print("Invalid choice. Please choose a valid number.")
                else:
                    selected_doctor = available_doctors.iloc[doctor_choice]
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # შეგვყავს პაციენტის აიდი დან ვიღებთ მონაცემებს ფაილიდან
        patient_id = input("Enter the patient's ID: ").strip()
        uid = 'a' + patient_id
        
        patients_df = pd.read_csv(self.patients_file, delimiter=';')
        
        patient_record = patients_df[patients_df['ID'] == uid]

        if patient_record.empty:
            print("Patient ID not found.")
            return

        patient_name = patient_record['Name'].values[0]
        patient_surname = patient_record['Surname'].values[0]
        patient_history = patient_record['history'].values[0]

        # ვქმნით ვიზიტის ჩანიშვნის დატაფრეიმს
        appointment_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        appointment_entry = {
            'timestamp': appointment_time,
            'doctor_id': selected_doctor['ID'],
            'doctor_name': f"Dr. {selected_doctor['Name']} {selected_doctor['Surname']}",
            'patient_id': uid,
            'patient_name': patient_name,
            'patient_surname': patient_surname,
            'medical_history': patient_history
        }

        new_appointment_df = pd.DataFrame([appointment_entry])

        # ვამოწმებტ ფაილის არსებობს თუ არა
        if os.path.exists(self.appointments_file):
            # თუ არსებობს ვკითხულობთ და ვამოწმებთ არის თ არა შიგნით ჩანაწერი და შესაბამისად ვამატებთ/ვქმნით ახალ ჩანაწერს 
            if os.path.getsize(self.appointments_file) > 0:
                appointments_df = pd.read_csv(self.appointments_file, delimiter=';')
                combined_appointments_df = pd.concat([appointments_df, new_appointment_df], ignore_index=True)
            else:
                combined_appointments_df = new_appointment_df
        else:
            combined_appointments_df = new_appointment_df

        combined_appointments_df.to_csv(self.appointments_file, sep=';', index=False, mode='w', header=True)

        print("Appointment successfully recorded.")