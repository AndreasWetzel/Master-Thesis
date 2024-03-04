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




"""
ROI_liste = ['OpticNerve_L', 'OpticNerve_R']
ROI6 = ['SpinalCord']
ROI7 = ['Cochlea_L']

ROIs = [ROI_liste,ROI6, ROI7]

# Gå gjennom hver ROI-gruppe
for idx, ROIs_group in enumerate(ROIs):
    print(ROIs_group[0])
    print(idx)
    # Liste for å lagre D50-verdier for hver ROI-gruppe
    D50_values = []

    # Gå gjennom hver ROI i gruppen
    for ROI in ROIs_group:
        D50, D1 = find_Dose(excel_filbane, ROI)
        D50_values.append(D50)  # Legg til D50-verdiene for ROI i gruppen

    # Opprett et boxplot for den aktuelle ROI-gruppen
    for i, j in enumerate(D50_values):
        plt.boxplot(j)

    plt.show()"""
# Opprett et boxplot



"""ROI1 = ['OpticNerve_L', 'OpticNerve_R', 'OpticChiasm','BrainstemCore','BrainstemSurface','Retina_L','Retina_R']
ROI2 = ['Cochlea_L','Cochlea_R','Pituitary','Lens_L','Lens_R','SpinalCord']
ROI3 = ['LacrimalGland_L','LacrimalGland_R','Hippocampus_L','Hippocampus_R']
ROI4 = ['GTV','CTV']
ROI5 = ['Brain-GTV','Brain-CTV']
ROIs = [ROI1,ROI2,ROI3,ROI4,ROI5]#[ROI_liste,ROI6,ROI7,ROI4,ROI5]

box_colors = ['blue', 'green', 'pink', 'grey', 'red', 'orange','darkviolet']

# Gå gjennom hver ROI-gruppe
for idx, ROIs_group in enumerate(ROIs):
    # Liste for å lagre D50-verdier for hver ROI-gruppe
    D50_values = []
    D1_values = []

    # Gå gjennom hver ROI i gruppen
    for ROI in ROIs_group:
        D50, D1 = find_Dose(excel_filbane, ROI)
        D50_values.append(D50)
        D1_values.append(D1)    # Legg til D50-verdiene for ROI i gruppen

    # Opprett et boxplot for den aktuelle ROI-gruppen
    plt.figure()  # Opprett en ny figur for hver ROI-gruppe
    positions = range(1, len(ROIs_group) + 1)  # Definer posisjonene for hver boxplot

    # Tilordne en unik farge til hvert boxplot i gruppen
    for i, D50 in enumerate(D50_values):
        plt.boxplot(D50, positions=[positions[i]], patch_artist=True, boxprops=dict(facecolor=box_colors[i]))

    # Sett tittel og akseetiketter for D50-plottene
    plt.title(f'LET D50')
    plt.ylabel(r'$\frac{keV}{\mu m}$')

    # Plasser navnene (x-aksen etiketter) under plottet for D50
    text_y = -0.17 * (plt.ylim()[1] - plt.ylim()[0])
    for i, position in enumerate(positions):
        plt.text(position, text_y, ROIs_group[i], color=box_colors[i], ha='center')

    plt.show()

    # Opprett et boxplot for D1-verdiene
    for i, D1 in enumerate(D1_values):
        plt.boxplot(D1, positions=[positions[i]], patch_artist=True, boxprops=dict(facecolor=box_colors[i]))

    # Sett tittel og akseetiketter for D1-plottene
    plt.title(f'LET D1')
    plt.ylabel(r'$\frac{keV}{\mu m}$')

    # Plasser navnene (x-aksen etiketter) under plottet for D1
    text_y = -0.17 * (plt.ylim()[1] - plt.ylim()[0])
    for i, position in enumerate(positions):
        plt.text(position, text_y, ROIs_group[i], color=box_colors[i], ha='center')

    plt.show()"""
"""ROI1 = ['OpticChiasm','OpticNerve_L','OpticNerve_R','BrainstemCore','BrainstemSurface']
ROI2 = ['Lens_L','Lens_L.1','Lens_R','Lens_R.1']
#ROI3 = ['GTV','CTV','PTV']
ROI4 = ['LacrimalGland_L','LacrimalGland_R','Cochlea_R','Cochlea_R.1','Cochlea_R.2']
ROI5 = ['Retina_L','Retina_R','Hippocampus_L','Hippocampus_R','Pituitary','Pituitary.1']
ROI6 = ['SpinalCord','SpinalCord.1']
ROI7 = ['Cochlea_L','Cochlea_L.1','Cochlea_L.2']

all_ROI_lists = [ROI1,ROI2, ROI4,ROI5,ROI6,ROI7]


DC1 = [55,55,55,54,60]
DC2 = [10, 10, 10, 10]
DC4 = [25, 25, 45,45,45]
DC5 = [45,45,7.3,7.3,45,45]
DC6 = [50,50]
DC7 = [45,45,45]
DC8 = [0,0]
line_values_list = [DC1,DC2,DC4,DC5,DC6,DC7] #Dose constraints
box_colors = ['blue', 'green', 'pink', 'grey', 'red', 'orange']

# Loop gjennom hver ROI-liste og utfør plottingsoperasjonene
for i, ROI_lister in enumerate(all_ROI_lists):
    dose_box_50 = []
    dose_box_1 = []

    plt.figure(figsize=(14, 6))

    for j, ROI in enumerate(ROI_lister):
        D50, D1 = find_Dose(excel_filbane, ROI)


        dose_box_50.append(list(D50))

        dose_box_1.append(list(D1))

    # Samle boksdataene i en zip og konverter til liste

    # Loop gjennom boksdata og utfør plottingsoperasjoner
    for j, (data1, data2) in enumerate(box_total):
        positions = [j * 2 + 1, j * 2 + 2]
        plt.boxplot([data1, data2], positions=positions, labels=['Protoner', 'Fotoner'], patch_artist=True,
                    boxprops=dict(facecolor=box_colors[j]))

        if j < len(line_values_list[i]):  # Sjekk om det er nok verdier i line_values_list for den aktuelle ROI
            line_value = line_values_list[i][j]
            # Plasser individuelle hlines for hver ROI
            plt.hlines(y=[line_value], xmin=positions[0] - 0.5, xmax=positions[1] + 0.5, linestyle='--',
                       color=box_colors[j], label=f'Dose constraint  {line_value} [Gy]')

        text_y = -0.17 * (plt.ylim()[1] - plt.ylim()[0]) # Plasser navnet under hvert boxplot
        print('text_y=   ', text_y)
        plt.text((positions[0] + positions[1]) / 2, text_y, ROI_lister[j], ha='center', va='bottom', color=box_colors[j], fontsize=10)

    save_file = os.path.join(f'{all_ROI_lists[i]}.png')

    # Lagre plottet
    plt.ylabel('Dose [Gy]')
    plt.legend()  # Vis legenden
    plt.savefig(save_file)
    plt.show()
"""

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


ROI1 = ['OpticNerve_L', 'OpticNerve_R', 'OpticChiasm','BrainstemCore','BrainstemSurface','Retina_L','Retina_R']
ROI2 = ['Cochlea_L','Cochlea_R','Pituitary','Lens_L','Lens_R','SpinalCord']
ROI3 = ['LacrimalGland_L','LacrimalGland_R','Hippocampus_L','Hippocampus_R']
ROI4 = ['GTV','CTV']
ROI5 = ['Brain-GTV','Brain-CTV']
ROI6 = ['OpticChiasm_50Gy','OpticNerve_L_50Gy','OpticNerve_R_50Gy']
ROI7 = ['Brain-GTV_50Gy','Brain-CTV_50Gy','GTV_50Gy','CTV_50Gy']
ROI8 = ['BrainstemCore_50Gy','BrainstemSurface_50Gy','Hippocampus_L_50Gy']
ROI9 = ['Cochlea_L_50Gy','Hippocampus_R_50Gy']
ROIs = [ROI6,ROI7,ROI8,ROI9]#[ROI_liste,ROI6,ROI7,ROI4,ROI5]

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
    save_file = os.path.join('boxplots_LET', f'{ROIs[idx]}_D50.png')
    plt.figure(figsize=(14, 6))  # Opprett en ny figur for hver ROI-gruppe
    positions = range(1, len(ROIs_group) + 1)  # Definer posisjonene for hver boxplot

    # Tilordne en unik farge til hvert boxplot i gruppen
    for i, D50 in enumerate(D50_values):
        plt.boxplot(D50, positions=[positions[i]], patch_artist=True, boxprops=dict(facecolor=box_colors[i]))


    plt.xticks(positions, ROIs_group, color='k')
    #plt.xticks(positions, ["" for _ in positions])

    # Sett tittel og akseetiketter
    plt.title(f'LET D50')
    #plt.xlabel('ROI', color='black')
    plt.ylabel(r'$\frac{keV}{\mu m}$')

    # Plasser navnene (x-aksen etiketter) under plottet
    """text_y = -0.1 * (plt.ylim()[1] - plt.ylim()[0])
    for i, position in enumerate(positions):
        plt.text(position, text_y, ROIs_group[i], color=box_colors[i], ha='center')"""

    #plt.legend()
    plt.savefig(save_file)

    plt.show()
    save_file = os.path.join('boxplots_LET', f'{ROIs[idx]}_D1.png')

    plt.figure(figsize=(14, 6))
    for i, D1 in enumerate(D1_values):
        plt.boxplot(D1, positions=[positions[i]], patch_artist=True, boxprops=dict(facecolor=box_colors[i]))






    plt.xticks(positions, ROIs_group, color='k')

    # Sett tittel og akseetiketter
    plt.title(f'LET D1')
    #plt.xlabel('ROI', color='black')
    #plt.ylabel('D50-verdi')
    plt.ylabel(r'$\frac{keV}{\mu m}$')

    # Plasser navnene (x-aksen etiketter) under plottet
    '''text_y = -0.1 * (plt.ylim()[1] - plt.ylim()[0])
    for i, position in enumerate(positions):
        plt.text(position, text_y, ROIs_group[i], color=box_colors[i], ha='center')'''


    plt.savefig(save_file)
    plt.show()
