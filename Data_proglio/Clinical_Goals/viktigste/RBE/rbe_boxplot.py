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

excel_filbane = 'RBE_vektet_dose.xlsx'
ROI1 = ['OpticNerve_L', 'OpticNerve_R', 'OpticChiasm']
ROI2 = ['BrainstemCore','BrainstemSurface','Retina_L','Retina_R']
ROI3 = ['LacrimalGland_L','LacrimalGland_R']
ROI4 = ['Pituitary','Hippocampus_L','Hippocampus_R']
ROI5 = ['CTV','GTV']
ROI6 = ['Cochlea_L','Cochlea_R']
ROI7 = ['SpinalCord']
ROI8 = ['Brain-GTV','Brain-CTV']
ROI9 = ['Lens_L','Lens_R']
'''ROI2 = ['Cochlea_L','Cochlea_R','Pituitary','Lens_L','Lens_R','SpinalCord']
ROI3 = ['LacrimalGland_L','LacrimalGland_R','Hippocampus_L','Hippocampus_R']
ROI4 = ['GTV','CTV']
ROI5 = ['Brain-GTV','Brain-CTV']'''
ROIs = [ROI1,ROI2,ROI3,ROI4,ROI5,ROI6,ROI7,ROI8,ROI9]#[ROI_liste,ROI6,ROI7,ROI4,ROI5]

box_colors = ['blue', 'green', 'pink', 'grey', 'red', 'orange','darkviolet']


# Gå gjennom hver ROI-gruppe
for idx, ROIs_group in enumerate(ROIs):
    # Liste for å lagre D50-verdier for hver ROI-gruppe
    D50_values = []
    D1_values = []

    # Gå gjennom hver ROI i gruppen
    for ROI in ROIs_group:
        D50, D1 = find_Dose(excel_filbane, ROI)
        D50_values.append(D50)  # Legg til D50-verdiene for ROI i gruppen
        D1_values.append(D1)
    # Opprett et boxplot for den aktuelle ROI-gruppen
    save_file = os.path.join('boxplot_rbe', f'{ROIs[idx]}_D50.png')
    plt.figure(figsize=(14, 6))  # Opprett en ny figur for hver ROI-gruppe
    positions = range(1, len(ROIs_group) + 1)  # Definer posisjonene for hver boxplot

    # Tilordne en unik farge til hvert boxplot i gruppen
    for i, D50 in enumerate(D50_values):
        plt.boxplot(D50, positions=[positions[i]], patch_artist=True, boxprops=dict(facecolor=box_colors[i]))


    plt.xticks(positions, ROIs_group, color='k')
    #plt.xticks(positions, ["" for _ in positions])

    # Sett tittel og akseetiketter
    plt.title(f'RBE vektet dose D50')
    #plt.xlabel('ROI', color='black')
    plt.ylabel('Dose [Gy(RBE)]')

    # Plasser navnene (x-aksen etiketter) under plottet
    """text_y = -0.1 * (plt.ylim()[1] - plt.ylim()[0])
    for i, position in enumerate(positions):
        plt.text(position, text_y, ROIs_group[i], color=box_colors[i], ha='center')"""

    #plt.legend()
    plt.savefig(save_file)

    plt.show()
    save_file = os.path.join('boxplot_rbe', f'{ROIs[idx]}_D1.png')

    plt.figure(figsize=(14, 6))
    for i, D1 in enumerate(D1_values):
        plt.boxplot(D1, positions=[positions[i]], patch_artist=True, boxprops=dict(facecolor=box_colors[i]))






    plt.xticks(positions, ROIs_group, color='k')

    # Sett tittel og akseetiketter
    plt.title(f'RBE vektet dose D1')
    #plt.xlabel('ROI', color='black')
    #plt.ylabel('D50-verdi')
    plt.ylabel('Dose [Gy(RBE)]')

    # Plasser navnene (x-aksen etiketter) under plottet
    '''text_y = -0.1 * (plt.ylim()[1] - plt.ylim()[0])
    for i, position in enumerate(positions):
        plt.text(position, text_y, ROIs_group[i], color=box_colors[i], ha='center')'''


    plt.savefig(save_file)
    plt.show()
