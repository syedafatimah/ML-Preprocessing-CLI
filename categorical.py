# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:39:43 2022

@author: Syeda Fatima Zahid
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from data_description import DataDescription

class Categorical:
    # The Task associated with this class.
    tasks = [
        '\n1. Show Categorical Columns',
        '2. Perform One Hot encoding',
        '3. Show whole Dataset'
    ]
    def __init__(self, data):
        self.data = data
        
    def categoricalColumn(self):
        print('\n{0: <20}'.format("Categorical Column") + '{0: <5}'.format("Unique Values"))
        # select_dtypes selects the columns with object datatype(which could be further categorize)
        for column in self.data.select_dtypes(include="object"):
            print('{0: <20}'.format(column) + '{0: <5}'.format(self.data[column].nunique()))

    def encoding(self):
        categorical_columns = self.data.select_dtypes(include="object")
        while(1):
            column = input("\nWhich column would you like to one hot encode?(Press -1 to go back)  ").lower()
            if column == "-1":
                break
            # The encoding function is only for categorical columns.
            if column in categorical_columns:
                self.data = pd.get_dummies(data=self.data, columns = [column])
                print("Encoding is done.")
                
                choice = input("Are there more columns to be encoded?(y/n)  ")
                if choice == "y" or choice == "Y":
                    continue
                else:
                    self.categoricalColumn()
                    break
            else:
                print("Wrong Column Name.")

    # The main function of the Categorical class.
    def categoricalMain(self):
        while(1):
            print("\nList of tasks:")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required.")
                    continue
                break

            if choice == -1:
                break
            
            elif choice == 1:
                self.categoricalColumn()

            elif choice == 2:
                self.categoricalColumn()
                self.encoding()

            elif choice == 3:
                DataDescription.showDataset(self)

            else:
                print("\nWrong Integer value!! Try again..")
        # return the data after modifying
        return self.data