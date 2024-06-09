import pandas as pd
from insurance import Insurance
from datetime import datetime

class AllServices:
    def __init__(self):
        pass
    #მომსახურების მიბმა პაციენტზე მისი სადაზღვეო ლიმიტის გათვალისწინებით
    def select_services(self):
        #ფუნქციის ბაზები .csv ფილები
        selected_services = []
        service_file = 'services.csv'
        patient_file = 'patients.csv'
        
        #პაციენტის აიდის შეყვანა
        patient_id = input("Please enter the patient's ID: ").strip()  
        
        uid = 'a' + patient_id
        
        #პაციენტის ფაილის წაკითხვა და დატაფრეიმში გადაყვანა
        patients_df = pd.read_csv(patient_file, delimiter=';')
        
        #print(patients_df['ID'].values)
        
        #ვეძებთ აიდის დატაფრეიმში
        if uid not in patients_df['ID'].astype(str).str.strip().values:
            print("Patient ID not found.")
            return
        
        #ვიღებთ სადაზღვეოს დაფარვის % ს პაციენტის მონაცემებიდან
        coverage_percentage = patients_df.loc[patients_df['ID'].astype(str).str.strip() == uid, 'Insurance covarage'].iloc[0]
        
        #ვკითხულობთ სერვის ფაილს. და გადაგვაქვს დატაფრეიმში
        df = pd.read_csv(service_file, delimiter=';')  
        
        #print("Header Row:")
        #print(df.columns.tolist())  
        
        #ვბეჭდავთ სერვისების სიას
        print("\nList of Services:")
        for idx, row in df.iterrows():
            print(f"{idx + 1}:", row.tolist())
        #ვსვავთ ლუუპში რომ საშალება გვქონდეს რამოდენიმე სერვისი დავამატოთ
        while True:
            choice = int(input("\nEnter the index of the service you want: ")) - 1
            
            if choice < 0 or choice >= len(df):
                print("Invalid index. Please choose a valid index.")
                continue
        
            selected_service = df.iloc[choice]
            print("\nYou have selected the following service:")
            
        
            selected_services.append(selected_service)
            print(selected_service)
            another_choice = input("\nDo you want to choose another service? (yes/no): ").lower()
            if another_choice != 'yes':
                break
        #ვანგარიშობთ მომსახურების მთლიან ჯამს
        total_cost = sum(selected_service['cost'] for selected_service in selected_services)
        print(f"\nTotal cost of selected services: {total_cost}")
        
        #ვუფარდებთ დაზღვევას
        insurance = Insurance(coverage_percentage)
        final_cost = Insurance.calculate_payment(insurance, total_cost)
        print(f"\nFinal cost of selected services is: {final_cost}")
        
        #ვიღებთ სერვისების ჩამონათვალს, ვამატებთ თაიმსტემპს 
        service_descriptions = [service[0] for service in selected_services]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_history_entry = f"{timestamp}: " + "; ".join(service_descriptions)
        
        #ვაფდეითებთ პაციენტის ფაილს
        patient_index = patients_df[patients_df['ID'].astype(str).str.strip() == uid].index[0]
        current_history = patients_df.at[patient_index, 'history']
        updated_history = (current_history + "; " + new_history_entry).strip("; ")
        patients_df.at[patient_index, 'history'] = updated_history
        
        
        patients_df.to_csv(patient_file, sep=';', index=False)
        
        print("Patient history updated successfully.")



