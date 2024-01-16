import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import copy

#Denne koden fungerer for å sammenlikne dose fra fotoner og protoner

def find_Dose(filbane, ROI, partikkel):
    df = pd.read_excel(filbane, header=None)
    funnede_verdier = []
    pas_nr = []

    for indeks, rad in df.iterrows():
        if ROI in rad.values and rad.iloc[1] == partikkel:
            #if rad.iloc[0] == 19 or rad.iloc[0] == 20 or rad.iloc[0] == 21:
            dose = rad.iloc[-1]
            pas = rad.iloc[0]
            pas_nr.append(pas)
            funnede_verdier.append(dose)

    return pas_nr, funnede_verdier


excel_filbane = 'Clinical_Golals_for_all_patients.xlsx'
ROI_liste = ['BrainstemSurface', 'Brain', 'Hippocampus_L','Hippocampus_R']
ROI_P = ['BrainstemSurface med protoner [Gy]', 'Brain med protoner [Gy]', 'Hippocampus_L med protoner [Gy]','Hippocampus_R med protoner [Gy]']
ROI_F = ['BrainstemSurface med fotoner [Gy]', 'Brain med fotoner [Gy]', 'Hippocampus_L med fotoner [Gy]', 'Hippocampus_R med fotoner [Gy]']

resultater_dict = {}

# Opprett en undermappe hvis den ikke allerede eksisterer
output_folder_protons_vs_photons = 'Plot_protons_photons'
if not os.path.exists(output_folder_protons_vs_photons):
    os.makedirs(output_folder_protons_vs_photons)

for ROI in ROI_liste:
    pas_nr_P, funnede_verdier_P = find_Dose(excel_filbane, ROI, 1)  # Pasienter med protoner
    funnede_verdier_P = [element * 1.1 for element in funnede_verdier_P] #Ganger med RBE1.1


    pas_nr_F, funnede_verdier_F = find_Dose(excel_filbane, ROI, 0)  # Pasienter med fotoner


    max_length = max(len(pas_nr_P), len(funnede_verdier_P), len(pas_nr_F), len(funnede_verdier_F))

    pas_nr_P += [np.nan] * (max_length - len(pas_nr_P))
    funnede_verdier_P += [np.nan] * (max_length - len(funnede_verdier_P))
    pas_nr_F += [np.nan] * (max_length - len(pas_nr_F))
    funnede_verdier_F += [np.nan] * (max_length - len(funnede_verdier_F))

    for i in range(len(ROI_P)):
        resultater_dict[ROI] = {'Pasientnummer med protoner': pas_nr_P,
                                ROI_P[i]: funnede_verdier_P,
                                'Pasientnummer med fotoner': pas_nr_F,
                                ROI_F[i]: funnede_verdier_F}

    protons = np.nanmean(funnede_verdier_P)
    photons = np.nanmean(funnede_verdier_F)

    plt.bar('Protons', protons)
    plt.bar('Photons', photons)
    plt.ylabel('Average dose [Gy]')
    plt.title(f'Comparison of the dose from protons and photons for {ROI}')

    # Lagre plottet som en fil i undermappen
    plt.savefig(os.path.join(output_folder_protons_vs_photons, f'ROI_{ROI}.png'))

    # Vis plottet
    plt.show()


# Opprett separate DataFrames for hver ROI
df_brainstem = pd.DataFrame(resultater_dict['BrainstemSurface'])
df_brain = pd.DataFrame(resultater_dict['Brain'])
df_hippo_L = pd.DataFrame(resultater_dict['Hippocampus_L'])
df_hippo_R = pd.DataFrame(resultater_dict['Hippocampus_R'])
# Skriv dataene til separate Excel-filer
output_brainstem_path = 'Dose_Brainstem.xlsx'
output_brain_path = 'Dose_Brain.xlsx'
output_hippo_L = 'Dose_Hippocampus_L.xlsx'
output_hippo_R = 'Dose_Hippocampus_R.xlsx'

df_brainstem.to_excel(output_brainstem_path, index=False)
df_brain.to_excel(output_brain_path, index=False)
df_hippo_L.to_excel(output_hippo_L, index=False)
df_hippo_R.to_excel(output_hippo_R, index=False)
'''

#Sammenlikner plassering av tumor og dose
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def find_Dose(filbane, ROI):
    df = pd.read_excel(filbane, header=None)
    funnede_verdier_113 = []
    funnede_verdier_123 = []

    xyz113 = [] #Venstre, oppe, midten
    xyz121 = [] #Venstre, nede, foran
    xyz122 = [] #Venstre, nede, bak
    xyz123 = [] #Venstre, nede, midten
    xyz132 = [] #Venstre, midten, bak
    #xyz211 = [] #høyre, oppe, foran
    #xyz212 = [] #høyre, oppe, bak
    xyz213 = [] #høyre, oppe, midten
    xyz221 = [] #høyre, nede, foran
    xyz223 = [] #høyre, nede, midten
    xyz231 = [] #Høyre, midten, fremme
    xyz233 = [] #høyre, midten, midten
    xyz311 = [] #midten, oppe, foran
    #xyz312 = [] #midten, oppe, bak
    xyz313 = [] #Midten, oppen, midten
    #xyz321 = [] #midten, nede, foran
    #xyz322 = [] #midten, nede, bak
    #xyz323 = [] #midten, nede, bak
    xyz331 = [] #Midten, midten, fremme
    xyz_name = ['vom','vnf', 'vnb', 'vnm', 'vmb', 'hom', 'hnf', 'hnm', 'hmf', 'hmm', 'hof', 'mom', 'mmf']
    for indeks, rad in df.iterrows():
        if ROI in rad.values:
            if rad.iloc[0] == 1 or rad.iloc[0] == 18:
            #if rad.iloc[0] == 19 or rad.iloc[0] == 20 or rad.iloc[0] == 21:
                dose = rad.iloc[-1]
                xyz113.append(dose)
            if rad.iloc[0] == 2:
                dose = rad.iloc[-1]
                xyz121.append(dose)
            if rad.iloc[0] == 7:
                dose = rad.iloc[-1]
                xyz122.append(dose)
            if rad.iloc[0] == 15:
                dose = rad.iloc[-1]
                funnede_verdier_123.append(dose)
            if rad.iloc[0] == 15:
                dose = rad.iloc[-1]
                xyz123.append(dose)
            if rad.iloc[0] == 11 or rad.iloc[0] == 19:
                dose = rad.iloc[-1]
                xyz132.append(dose)
            if rad.iloc[0] == 20 or rad.iloc[0] == 29:
                dose = rad.iloc[-1]
                xyz213.append(dose)
            if rad.iloc[0] == 5 or rad.iloc[0] == 10 or rad.iloc[0] == 14:
                dose = rad.iloc[-1]
                xyz221.append(dose)
            if rad.iloc[0] == 24 or rad.iloc[0] == 25 or rad.iloc[0] == 27:
                dose = rad.iloc[-1]
                xyz223.append(dose)
            if rad.iloc[0] == 17:
                dose = rad.iloc[-1]
                xyz231.append(dose)
            if rad.iloc[0] == 8 or rad.iloc[0] == 13 or rad.iloc[0] == 26:
                dose = rad.iloc[-1]
                xyz233.append(dose)
            if rad.iloc[0] == 22 or rad.iloc[0] == 23:
                dose = rad.iloc[-1]
                xyz311.append(dose)
            if rad.iloc[0] == 6 or rad.iloc[0] == 16:
                dose = rad.iloc[-1]
                xyz313.append(dose)
            if rad.iloc[0] == 9 or rad.iloc[0] == 21 or rad.iloc[0] == 29:
                dose = rad.iloc[-1]
                xyz331.append(dose)


    return xyz113, xyz121, xyz122, xyz123, xyz132, xyz213, xyz221, xyz223, xyz231, xyz233, xyz311, xyz313, xyz331


excel_filbane = 'Clinical_Golals_for_all_patients.xlsx'
ROI_liste = ['BrainstemSurface','GTV']#, 'Brain', 'Hippocampus_L','Hippocampus_R']
xyz_name = ['vom','vnf', 'vnb', 'vnm', 'vmb', 'hom', 'hnf', 'hnm', 'hmf', 'hmm', 'hof', 'mom', 'mmf']


resultater_dict = {}

# Opprett en undermappe hvis den ikke allerede eksisterer
output_folder_location_of_tumor = 'Plots_location_of_tumor'
if not os.path.exists(output_folder_location_of_tumor):
    os.makedirs(output_folder_location_of_tumor)

for ROI in ROI_liste:
    x = []
    x.append(find_Dose(excel_filbane, ROI))
    print(x)

    for i in range(len(x)):
        # Iterer over indeksene i stedet for verdiene
        max_length = max(len(row) for row in x[i])  # Finne maks lengde i listen av lister

        # Opprett en ny liste med NaN-verdier og legg den til i x[i]
        x[i] = [row + [np.nan] * (max_length - len(row)) for row in x[i]]

        # Gjennomsnittet av hvert sett med tall
        mean_values = [np.nanmean(row) for row in x[i]]
        print(mean_values)


        # Gjennomsnittet av alle tallene i x[i]
        overall_mean = np.nanmean(mean_values)
        print(f'Overall mean for {ROI}: {overall_mean}')

        # Plott mean values med stolpediagram (bar plot)
        plt.bar([f'{j}' for j in xyz_name], mean_values, alpha=1)

    # Vis stolpediagrammet
    plt.ylabel('Mean Dose [Gy]')
    plt.title(f'Comparison of Mean Values for {ROI}')
    plt.savefig(os.path.join(output_folder_location_of_tumor, f'ROI_{ROI}.png'))
    plt.show()
'''
