# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:46:38 2022

@author: Syeda Fatima Zahid
"""

import pandas as pd

class DataDescription:
    tasks = [
        '\n1. Describe a specific Column',
        '2. Show Properties of Each Column',
        '3. Show the Dataset'
    ]
    
    def __init__(self, data):
        self.data = data
        
    def showDataset(self):
        while(1):
            try:
                rows = int(input(("\nHow many rows(>0) to print? (Press -1 to go back)  ")))
                if rows == -1:
                    break
                if rows <= 0:
                    print("Number of rows given must be +ve...")
                    continue
                print(self.data.head(rows))
            except ValueError:
                print("Numeric value is required. Try again....")
                continue
            break
        return
    
    def showColumns(self):
        for column in self.data.columns.values:
            print(column, end = " ")
            
    def describe(self):
        while(1):
            print("\nTasks (Data Description)")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required.")
                    continue
                break

            if choice==-1:
                break
                        
            elif choice==1:
                self.showColumns()
                while(1):
                    describeColumn = input("\n\nWhich Column?  ").lower()
                    try:
                        # describe() function is used to tell all the info regarding any specific column.
                        print(self.data[describeColumn].describe())
                    except KeyError:
                        print("No Column present with this name.")
                        continue
                    break
            
            elif choice==2:
                # describe() function is used to tell all the info about the database.
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())

            elif choice==3:
                self.showDataset()

            else:
                print("\nWrong Integer value!! Try again..")