"""
import pandas as pd
import numpy as np
import random
from data_structure import patient_columns, patient_history_columns,staff_columns,service_columns

class FileManager:
    def __init__(self, file_n):
        self.file_n = file_n
        self.df = pd.DataFrame()
        
    
    def create_file(self, specific_columns): #კოლონების სახელებს აიღებს იმს დამიხედვით თ რა ფაილს ქმნის
        self.df = pd.DataFrame(columns=specific_columns)
        self.df.to_csv(self.file_n, index=False)

    def add_to_file(self, data): #data რაც უნდა დაემატოს
        new_df = pd.DataFrame(data)
        self.df = pd.concat([self.df, new_df], ignore_index=True)
        self.df.to_csv(self.file_n, index=False)

    def remove_from_file (self, ID):
        self.df = pd.read_csv(self.file_n)
        self.df = self.df[self.df['ID']!=ID]
        self.df.to_csv(self.file_n, index = False)

    def update_information_in_file (self, ID, new_data):
        self.df = pd.read_csv(self.file_n)
        self.df.loc[self.df['ID']==ID] = new_data
        self.df.to_csv(self.file_n, index = False)
        
    def read_file (self):
        self.df = pd.read_csv(self.file_n)
        return self.df
"""