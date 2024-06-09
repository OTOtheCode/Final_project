
import pandas as pd
from insurance import Insurance
class AllServices:
    @staticmethod
    def selec_services(filename, patient):
        selected_services = []  
    
        
        df = pd.read_csv(filename, delimiter=';')  
    
        
        print("Header Row:")
        print(df.columns.tolist())  
    
        
        print("\nList of Services:")
        for idx, row in df.iterrows():
            print(f"{idx + 1}:", row.tolist())
    
        while True:
            
            choice = int(input("\nEnter the index of the service you want: ")) - 1
        
            
            if choice < 0 or choice >= len(df):
                print("Invalid index. Please choose a valid index.")
                continue
        
            
            selected_service = df.iloc[choice]
            print("\nYou have selected the following service:")
            print(selected_service)
        
            
            selected_services.append(selected_service)
        
            
            another_choice = input("\nDo you want to choose another service? (yes/no): ").lower()
            if another_choice != 'yes':
                break
    
        total_cost = sum(selected_service['cost'] for selected_service in selected_services)
        print(f"\nTotal cost of selected services: {total_cost}")
        a = int(input('please enter covarage percentage of insurance :'))
        insurance = Insurance(a)
        final_cost = Insurance.calculate_payment(insurance, total_cost)
        print(f"\nFinal cost of selected services is: {final_cost}")
          

AllServices.selec_services('services.csv', 'patients.csv')
