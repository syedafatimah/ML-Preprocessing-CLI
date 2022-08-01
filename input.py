# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:39:07 2022

@author: Syeda Fatima Zahid
"""

#import libraries
from os import path
import sys
import pandas as pd

#argv
class data_input:
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    #extensions supported for input file
    supported_file_extensions = [
        '.csv',
    ]
    
    # convert column names into lower case
    def convert_to_lowercase(self, data):
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
        return data
    
    def input_function(self):
        try:
           filename, file_extension = path.splitext(sys.argv[1])
           if file_extension == "":
               raise SystemExit(f"Provide the " + self.bold_start + "DATASET" + self.bold_end +" name (with extension).\U0001F643")

           if file_extension not in self.supported_file_extensions:
               raise SystemExit(f"This file extension is not " + self.bold_start + "supported.\U0001F643" + self.bold_end)
       
        except IndexError:
           raise SystemExit(f"Provide the " + self.bold_start + "DATASET" + self.bold_end +" name (with extension).\U0001F643")
       
        try:
           data = pd.read_csv(filename+file_extension)
        except pd.errors.EmptyDataError:
           raise SystemExit(f"The file is "+ self.bold_start + "EMPTY" + self.bold_end + "\U0001F635")

        except FileNotFoundError:
           raise SystemExit(f"File " + self.bold_start + "doesn't" + self.bold_end + " exist\U0001F635")

        data = self.convert_to_lowercase(data)

        return data