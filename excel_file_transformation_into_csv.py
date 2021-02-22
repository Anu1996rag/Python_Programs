# -*- coding: utf-8 -*-


#argv method from the sys library takes out the arguments from the console and helps in handling 
#command line arguments
from sys import argv 
from pandas import read_excel
#read_excel takes argument as the file path which is an excel file

#taking the file path from the command line argument interface
#here 1 represents the file path after the program name  which is represented as 0

file_path = argv[1]

#renaming the file destination path 
#below line renames the destination path 
#example : if the source path is D:\users\sbc.xls , it will renamed as D:\users\abc.csv
try:
    destination_file_name = file_path.replace("xlsx","csv").replace("xls","csv")
    #above code will check for both possible file extensions "xlsx or xls" and will replace with the csv extension
        
    #reading the file from the path 
    #this will read the excel file name from the file path 
    file_read = read_excel(file_path)
    
    #below code converts the excel file into csv file 
    file_read.to_csv(destination_file_name,index=False)
    print("File successfully written.",destination_file_name)
except :
    print("File Not Found",file_path)
    







