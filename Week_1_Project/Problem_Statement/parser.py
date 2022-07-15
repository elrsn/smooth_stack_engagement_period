# Author: Elliott Larsen
# Date:
# Description: 

import glob
import os
import openpyxl as op
import logging

# Set up logger and directory.
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
directory_path = r"/Users/name/Desktop/SmoothStack/smooth_stack_engagement_period/Week_1_Project/Problem_Statement/"

# In case of an invalid/incorrect directory path.
try:
    os.chdir(directory_path)
except Exception as e: 
    # Shoult it be logging.error?
    logging.error(e)

# Create a list of workbook objects from the directory.
xlsx_file_lst = []
workbook_obj_lst = []
for file in glob.glob("*.xlsx"):
    wb = op.load_workbook(directory_path + file)
    workbook_obj_lst.append(wb)

# If there is no .xlsx file in the directory.
try:
    temp_var = workbook_obj_lst[0]
except IndexError as e:
    logging.error(f"There is no .xlsx file in this directory.  Error message: {e}")
