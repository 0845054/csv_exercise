import pandas as pd
import os
import statistics


# Variables
# Update csv_file to target CSV File name.
# Ensure the csv file is in current working directory.
# Update col_dict base on the possible Columns Types
csv_file = 'addresses.csv'
csv_path = f'{os.getcwd()}\{csv_file}'
col_dict = {'Postal': 0, 'Name': 1, 'Address': 2}


# Takes in a String and return the possible Column Type
def typeCheck(val: str):
    col_types = list(col_dict.keys())

    # Postal code check
    if val.isnumeric(): val_type = col_types[0] 

    # Name check
    elif val.isalpha(): val_type = col_types[1]

    # Contains both numberic and alpha, conclude Address.
    else: val_type = col_types[2]

    return val_type

# Takes in an Item and use col_dict to returns it's Key. 
def getKey(val):
    for key,item in col_dict.items():
        if item == val:
            return key

def main():

    # Update range base on the number of columns in CSV File.
    count = [[] for i in range(6)]
    df = pd.read_csv(csv_path)
    for idx, row in df.iterrows():
        for i in range(len(row)):
            cur_type = typeCheck(str(row[i]))
            count[i].append(col_dict[cur_type])
          
    ans = []
    for x in count:
        most_common = statistics.mode(x) 
        ans.append(getKey(most_common))
       
    print(ans)  
    return

main()