


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
    parameter = []


    for indeks, rad in df.iterrows():
        if ROI in rad.values and rad.iloc[1] == partikkel:
            #if rad.iloc[0] == 19 or rad.iloc[0] == 20 or rad.iloc[0] == 21:
            dose = rad.iloc[-1] #Gitt dose
            pas = rad.iloc[0] #Pasient nummer
            par = rad.iloc[-2] #Kriterier
            pas_nr.append(str(pas))
            funnede_verdier.append(dose)
            parameter.append(par)



    return pas_nr, funnede_verdier, parameter


excel_filbane = 'doser.xlsx'
ROI_liste = ['OpticChiasm','OpticNerve_L','OpticNerve_R','BrainstemCore','BrainstemSurface',
            'SpinalCord','SpinalCord.1','GTV','Brain-GTV','CTV','Brain-CTV','PTV','Retina_L','Retina_R',
            'Cochlea_L','Cochlea_L.1','Cochlea_L.2','Cochlea_R','Cochlea_R.1','Cochlea_R.2','Pituitary',
            'Pituitary.1','Lens_L','Lens_L.1','Lens_R','Lens_R.1','LacrimalGland_L','LacrimalGland_R',
            'Hippocampus_L','Hippocampus_R']

#ROI_liste = ['LacrimalGland_L','LacrimalGland_R','Hippocampus_L','Hippocampus_R']
print(len(ROI_liste))
#ROI_liste_ = ['SpinalCord','SpinalCord.1']
#ROI_liste = ['BrainstemSurface', 'Brain', 'Hippocampus_L','Hippocampus_R']
ROI_P = ['BrainstemSurface med protoner [Gy]', 'Brain med protoner [Gy]', 'Hippocampus_L med protoner [Gy]','Hippocampus_R med protoner [Gy]']
ROI_F = ['BrainstemSurface med fotoner [Gy]', 'Brain med fotoner [Gy]', 'Hippocampus_L med fotoner [Gy]', 'Hippocampus_R med fotoner [Gy]']


resultater_dict = {}
organ_kriterier = {}

'''dose_box_P = []
dose_box_F = []'''

# Opprett en undermappe hvis den ikke allerede eksisterer
output_folder_protons_vs_photons = 'Plot_protons_photons'
if not os.path.exists(output_folder_protons_vs_photons):
    os.makedirs(output_folder_protons_vs_photons)

for ROI in ROI_liste:
    pas_nr_P, funnede_verdier_P, kriterie_P = find_Dose(excel_filbane, ROI, 1)  # Pasienter med protoner
    funnede_verdier_P = [element * 1.1 for element in funnede_verdier_P] #Ganger med RBE1.1
    #dose_box_P.append(list(funnede_verdier_P))

    pas_nr_F, funnede_verdier_F, kriterie_F = find_Dose(excel_filbane, ROI, 0)  # Pasienter med fotoner


    #dose_box_F.append(list(funnede_verdier_F))

    antall_pasienter_P = len(pas_nr_P)
    antall_pasienter_F = len(pas_nr_F)
    max_length = max(len(pas_nr_P), len(funnede_verdier_P), len(pas_nr_F), len(funnede_verdier_F),len(kriterie_P),len(kriterie_F))

    pas_nr_P += [np.nan] * (max_length - len(pas_nr_P))
    funnede_verdier_P += [np.nan] * (max_length - len(funnede_verdier_P))
    kriterie_P += [np.nan] * (max_length - len(kriterie_P))
    #antall_pasienter_P += [np.nan] * (max_length - len(antall_pasienter_P))

    pas_nr_F += [np.nan] * (max_length - len(pas_nr_F))
    funnede_verdier_F += [np.nan] * (max_length - len(funnede_verdier_F))
    kriterie_F += [np.nan] * (max_length - len(kriterie_F))
    #antall_pasienter_F += [np.nan] * (max_length - len(antall_pasienter_F))

    for i in range(len(ROI_P)):
        resultater_dict[ROI] = {'Pasientnummer med protoner': pas_nr_P,
                                ROI_P[i]: funnede_verdier_P,
                                'Pasientnummer med fotoner': pas_nr_F,
                                ROI_F[i]: funnede_verdier_F}

        organ_kriterier[ROI] = {'Organ': ROI, "Kriterier": kriterie_F,
                                'Pasientnummer med protoner': pas_nr_P,
                                'Pasientnummer med fotoner': pas_nr_F,
                                "N_p": antall_pasienter_P,
                                "N_f": antall_pasienter_F}

'''print('Box protoner', dose_box_P)
print('Box fotoner', dose_box_F)
box_zip = zip(dose_box_P,dose_box_F)
box_total = list(box_zip)
print('-------------------------')
print('Total box: ', box_total)

print('--------------------')
print(box_total[0][0])'''







'''ROI_liste_2 = ['GTV','Brain-GTV','CTV','PTV','Hippocampus_L','Hippocampus_R','LacrimalGland_L','LacrimalGland_R']

ROI_liste_3 = ['SpinalCord','SpinalCord.1','Cochlea_L','Cochlea_L.1','Cochlea_L.2','Lens_L','Lens_L.1','Lens_R','Lens_R.1']'''
# Organiser alle ROI-lister i én liste

ROI1 = ['OpticChiasm','OpticNerve_L','OpticNerve_R','BrainstemCore','BrainstemSurface']
ROI2 = ['Lens_L','Lens_R']
#ROI3 = ['GTV','CTV','PTV']
ROI4 = ['LacrimalGland_L','LacrimalGland_R','Cochlea_L','Cochlea_R']
ROI5 = ['Retina_L','Retina_R','Hippocampus_L','Hippocampus_R','Pituitary']
ROI6 = ['SpinalCord']
ROI7 = ['Cochlea_L']

all_ROI_lists = [ROI1,ROI2, ROI4,ROI5,ROI6]


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
    dose_box_P = []
    dose_box_F = []

    plt.figure(figsize=(14, 6))

    for j, ROI in enumerate(ROI_lister):
        pas_nr_P, funnede_verdier_P, kriterie_P = find_Dose(excel_filbane, ROI, 1)  # Pasienter med protoner
        funnede_verdier_P = [element * 1.1 for element in funnede_verdier_P]  # Ganger med RBE1.1
        dose_box_P.append(list(funnede_verdier_P))

        pas_nr_F, funnede_verdier_F, kriterie_F = find_Dose(excel_filbane, ROI, 0)  # Pasienter med fotoner
        dose_box_F.append(list(funnede_verdier_F))

    # Samle boksdataene i en zip og konverter til liste
    box_zip = zip(dose_box_P, dose_box_F)
    box_total = list(box_zip)

    # Definer posisjonene for hvert sett med navn
    positions = [k * 2 + 1 for k in range(len(ROI_lister))]

    # Loop gjennom boksdata og utfør plottingsoperasjoner
    """for j, (data1, data2) in enumerate(box_total):
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

    # Sett navnene på x-aksen
    #plt.xticks(positions, ["" for _ in positions])  # Fjern standard x-akse etiketter

    save_file = os.path.join('word', f'{all_ROI_lists[i]}.png')

    # Lagre plottet
    plt.ylabel('Dose [Gy]')
    plt.legend(loc='upper left')  # Vis legenden
    plt.savefig(save_file)
    plt.show()"""

ROI8 = ['GTV','CTV','GTV_D2','CTV_D2']
ROI9 = ['Brain-GTV','Brain-CTV']
all_ROI_lists = [ROI8,ROI9]

h_line =[107,107,107,107]
Brain_GTV_CTV = [107,107,107,107]
line_values_list = [h_line,Brain_GTV_CTV]
for i, ROI_lister in enumerate(all_ROI_lists):
    dose_box_P = []
    dose_box_F = []

    for ROI in ROI_lister:
        pas_nr_P, funnede_verdier_P, kriterie_P = find_Dose(excel_filbane, ROI, 1)  # Pasienter med protoner
        funnede_verdier_P = [element * 1.1 for element in funnede_verdier_P] #Ganger med RBE1.1
        #dose_box_P.append(list(funnede_verdier_P))
        dose_box_P_precent = [value / 54 * 100 for value in funnede_verdier_P]
        dose_box_P.append(dose_box_P_precent)

        pas_nr_F, funnede_verdier_F, kriterie_F = find_Dose(excel_filbane, ROI, 0)  # Pasienter med fotoner
        dose_box_F_precent = [value / 54 * 100 for value in funnede_verdier_F]
        dose_box_F.append(dose_box_F_precent)


    # Samle boksdataene i en zip og konverter til liste
    box_zip = zip(dose_box_P, dose_box_F)
    box_total = list(box_zip)

    # Lag etiketter for plottet
    labels = [f"{ROI} med protoner [Gy]" for ROI in ROI_lister] + [f"{ROI} med fotoner [Gy]" for ROI in ROI_lister]

    plt.figure(figsize=(14, 6))

    # Loop gjennom boksdata og utfør plottingsoperasjoner
    for j, (data1, data2) in enumerate(box_total):
        positions = [j*2+1, j*2+2]
        plt.boxplot([data1, data2], positions=positions, labels=['Protoner', 'Fotoner'], patch_artist=True, boxprops=dict(facecolor=box_colors[j]))
        plt.text(positions[0], max(max(data1), max(data2)), all_ROI_lists[i][j], ha='center', va='bottom', color=box_colors[j], fontsize=10)

        if j < len(line_values_list[i]):  # Sjekk om det er nok verdier i line_values_list for den aktuelle ROI
            line_value = line_values_list[i][j]
            # Plasser individuelle hlines for hver ROI
            plt.hlines(y=[line_value], xmin=positions[0] - 0.5, xmax=positions[1] + 0.5, linestyle='--',
                       color=box_colors[j], label=f'Dose constraint  {line_value} [Gy]')
        text_y = -0.01 * (plt.ylim()[1] - plt.ylim()[0]) # Plasser navnet under hvert boxplot
        print('text_y=   ', text_y)
        #plt.text((positions[0] + positions[1]) / 2, text_y, ROI_lister[j], ha='center', va='bottom', color=box_colors[j], fontsize=10)

    save_file = os.path.join('word', f'{all_ROI_lists[i]}.png')

    # Lagre plottet
    plt.ylabel('% of prescribed dose')
    plt.legend(loc='upper left')
    plt.savefig(save_file)
    plt.show()



#Her finner du kriteriene på ønsket organ og hvilke pasienter som har fått samt antall
#pasienter med protoner og fotoner
# Lag DataFrames
df_frames = []


for i in ROI_liste:
    df = pd.DataFrame(organ_kriterier[i])
    df_frames.append(df)


print('------- HUSK Å LEGGE INN ROI_liste_ ---------')
'''for i in ROI_liste_:
    df = pd.DataFrame(organ_kriterier[i])
    df_frames.append(df)'''

# Slå sammen DataFrames ved å legge dem ved siden av hverandre (kolonnevis)
combined_df = pd.concat(df_frames, axis=0)

# Skriv dataene til en Excel-fil
output_combined_path = 'organ_kriterier.xlsx'
combined_df.to_excel(output_combined_path, index=False)

print(f"Dataene er slått sammen kolonnevis og lagret som {output_combined_path}")


'''# Opprett separate DataFrames for hver ROI
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
df_hippo_R.to_excel(output_hippo_R, index=False)'''
