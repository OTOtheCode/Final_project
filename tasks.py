import pandas as pd
import os

#დავალების მოდული
class Tasks:
    def __init__(self):
        pass    
      
    def assign_task(self, id, task):
        file_path = 'staff.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            df = pd.read_csv(file_path, sep=';')
            if id in df['ID'].values:
                df.loc[df['ID'] == id, 'Assigned_task'] = task
                df.to_csv(file_path, sep=';', index=False)
                staff_member = df[df['ID'] == id].iloc[0]
                print(f"Task '{task}' assigned to {staff_member['Position']} {staff_member['Name']} {staff_member['Surname']}.")
            else:
                print(f"Staff member with ID {id} not found.")
        else:
            print("Staff file does not exist or is empty.")
    