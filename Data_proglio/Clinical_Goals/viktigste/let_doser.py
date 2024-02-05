import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import copy


def find_Dose(filbane, ROI):
    df = pd.read_excel(filbane, header=None)
    D50 = []
    D1 = []


    for indeks, rad in df.iterrows():
        if ROI in rad.values:
            #if rad.iloc[0] == 19 or rad.iloc[0] == 20 or rad.iloc[0] == 21:
            d1 = rad.iloc[3] #Gitt dose
            d50 = rad.iloc[2] #Pasient nummer
            D50.append(d50)
            D1.append(d1)



    return D50, D1



excel_filbane = 'LET_dose_statistics.xlsx'
"""ROI_liste = ['OpticChiasm','OpticNerve_L','OpticNerve_R','BrainstemCore','BrainstemSurface',
            'SpinalCord','SpinalCord.1','GTV','Brain-GTV','CTV','Brain-CTV','PTV','Retina_L','Retina_R',
            'Cochlea_L','Cochlea_L.1','Cochlea_L.2','Cochlea_R','Cochlea_R.1','Cochlea_R.2','Pituitary',
            'Pituitary.1','Lens_L','Lens_L.1','Lens_R','Lens_R.1','LacrimalGland_L','LacrimalGland_R',
            'Hippocampus_L','Hippocampus_R']"""
ROI_liste = ['OpticNerve_L']

for ROI in ROI_liste:
    D50, D1 = find_Dose(excel_filbane, ROI)
    print(D50)

    plt.boxplot([D50, D1], labels=['D50', 'D2'])
    plt.title(f'Boxplot for {ROI}')
    plt.xlabel('Dose Type')
    plt.ylabel('Dose Values')
    plt.show()
