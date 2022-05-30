# -*- coding: utf-8 -*-
"""
Created on Sun May 29 16:11:40 2022

@author: anirudhya n
"""

import pandas as pd
#import sys

#src_file_path=sys.argv[2]
#mapping_file_path = sys.argv[1]
#tar_file_path = sys.argv[3]
mapping_file_path = "Mapping_Sheet.txt"
src_file_path = "Source_Data_employee.xlsx"
tar_file_path = "Target_Data_employee.xlsx"
src_pk_key_column = "emp_id"
tar_pk_key_column = "Employee_id"

with open(mapping_file_path,'r') as map_file:
    global mapping_dict 
    mapping_dict = {}
    for line in map_file:
        record=line.strip()
        if record.lower() != "source:target" and ":" in record :
            source_column = record.split(":")[0]
            target_column = record.split(":")[1]
            mapping_dict[source_column]=target_column
print("The Mapping dictionary is : ")
print(mapping_dict)

print("Reading the source file as a dataframe: ")
src_df = pd.read_excel(src_file_path)
print("The source data frame is : ")
print(src_df)
 
print("Reaing the target file as a datafrme: ")
tar_df = pd.read_excel(tar_file_path)
print("The target data frame is : ")
print(tar_df)

print("Starting data Validation :")
print("Checking for Record count in source and target:")
src_record_count = src_df.shape[0]
print("src_record_count:",src_record_count)
print("Type:",type(src_record_count))
tar_record_count = tar_df.shape[0]
print("tar_record_count:",tar_record_count)
print("Type:",type(tar_record_count))

if src_record_count == tar_record_count:
    print("Source record count:{}  Target record count: {} The counts are equal ".format(src_record_count,tar_record_count))
else:
    print("Source record count:{}  Target record count: {} The counts are not  equal ".format(src_record_count,tar_record_count))

print("Starting data validation :")

src_df = src_df.sort_values(by=[src_pk_key_column])
tar_df = tar_df.sort_values(by=[tar_pk_key_column])

src_pk_list = list(src_df[src_pk_key_column])
tar_pk_list = list(tar_df[tar_pk_key_column])

for i in src_pk_list:
    if i in tar_pk_list:
        for j in mapping_dict.keys():
            a = list(src_df[src_df[src_pk_key_column]==i][j])[0]
            b = list(tar_df[tar_df[tar_pk_key_column]==i][mapping_dict[j]])[0]
            if (a != b):
                print("id: {} source_column:{} source_value :{} target_column: {} target_value :{} Values are mismatching".format(i,j,a,mapping_dict[j],b))

    
            
    


            
    
