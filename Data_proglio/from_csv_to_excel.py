import csv
import pandas as pd
import numpy as np

'''
with open("Patient29_fotoner_Dose.csv", "r") as file:
    csvreader = csv.DictReader(file)

    organ_volume = []
    D99 = []
    D98 = []
    D50 = []
    D2 = []
    D1 = []
    D_ave = []
    ROI_vol = []

    for row in csvreader:
        organ_volume.append(row[" "])
        D99.append(float(row["D99"]))
        D98.append(float(row["D98"]))
        D50.append(float(row["D50"]))
        D2.append(float(row["D2"]))
        D1.append(float(row["D1"]))
        D_ave.append(float(row["Average Dose"]))
        ROI_vol.append(float(row["ROI Volume"]))


columns=['D99','D98','D50',"D2","D1","D Average", "ROI Volume"]

# Create DataFrame from multiple lists
df = pd.DataFrame(list(zip(D99,D98,D50,D2,D1,D_ave,ROI_vol)), index=organ_volume, columns=columns)
print(df)

# Write DataFrame to Excel file
df.to_excel('Patient29_Dose_statistics.xlsx')
'''

"""Fra patient 10 elns så fungerer ikke dose statestikk for fotoner"""

x = ["Patient1_Clinical_Goals.csv","Patient2_Clinical_Goals.csv","Patient5_Clinical_Goals.csv","Patient6_Clinical_Goals.csv","Patient8_Clinical_Goals.csv","Patient9_Clinical_Goals.csv","Patient14_Clinical_Goals.csv","Patient20_Clinical_Goals.csv","Patient21_Clinical_Goals.csv","Patient26_Clinical_Goals.csv","Patient27_Clinical_Goals.csv","Patient28_Clinical_Goals.csv","Patient29_Clinical_Goals.csv"]
y = ["Patient1_ClinicGoals.xlsx","Patient2_ClinicGoals.xlsx","Patient5_ClinicGoals.xlsx","Patient6_ClinicGoals.xlsx","Patient8_ClinicGoals.xlsx","Patient9_ClinicGoals.xlsx","Patient14_ClinicGoals.xlsx","Patient20_ClinicGoals.xlsx","Patient21_ClinicGoals.xlsx","Patient26_ClinicGoals.xlsx","Patient27_ClinicGoals.xlsx","Patient28_ClinicGoals.xlsx","Patient29_ClinicGoals.xlsx"]

for i in range(len(x)):
    data = pd.read_csv(x[i])
    print(data)
    data = data.T
    data.iloc[:,-1] = pd.to_numeric(data.iloc[:,-1],errors="coerce")

    df = pd.DataFrame((data))
    df.columns = ["Criteria", "Dose [Gy]"]

    df.to_excel(y[i])

'''
data = pd.read_csv("Patient29_fotoner_DoseD40.csv", header=None, names=['ROI', 'D40'])

# Skriv dataene til Excel-fil
data.to_excel('Patient29_D40.xlsx', index=False)


data = pd.read_csv("Patient29_fotoner_Dose_D003cc.csv")
#print(data)
data = data
data.iloc[:,-1] = pd.to_numeric(data.iloc[:,-1],errors="coerce")

df = pd.DataFrame((data))
df.columns = ["Volume","D0.03cc"]

df.to_excel('Patient29_D003cc.xlsx',index=False)
'''
"""
columns=['D99','D98','D50',"D2","D1","D Average", "ROI Volume"]
data = pd.read_csv("Patient29_fotoner_Dose.csv", header=None, names=columns)

# Skriv dataene til Excel-fil
data.to_excel('Patient29_Dose.xlsx', index=False)
"""
