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
            d50 = rad.iloc[-1] #Pasient nummer
            D50.append(d50)
            #D1.append(d1)



    return D50#, D1



excel_filbane = 'Clinical_goals_RBE11.xlsx'
excel_rorvik = 'RBE_Rorvik.xlsx'


ROI1 = ['OpticNerve_L', 'OpticNerve_R', 'OpticChiasm','BrainstemCore','BrainstemSurface','Retina_L','Retina_R']
ROI2 = ['Lens_L','Lens_R','LacrimalGland_L','LacrimalGland_R']
ROI3 = ['Hippocampus_L','Hippocampus_R','Pituitary']#'SpinalCord']
ROI4 = ['Cochlea_L','Cochlea_R']
ROI5 = ['SpinalCord']
ROI7 = ['GTV','CTV']
ROI6 = ['Brain-GTV','Brain-CTV']
"""ROI6 = ['OpticChiasm_50Gy','OpticNerve_L_50Gy','OpticNerve_R_50Gy']
ROI7 = ['Brain-GTV_50Gy','Brain-CTV_50Gy','GTV_50Gy','CTV_50Gy']
ROI8 = ['BrainstemCore_50Gy','BrainstemSurface_50Gy','Hippocampus_L_50Gy']
ROI9 = ['Cochlea_L_50Gy','Hippocampus_R_50Gy']"""
ROIs = [ROI1,ROI2,ROI3,ROI4,ROI5,ROI6,ROI7]#[ROI_liste,ROI6,ROI7,ROI4,ROI5]

file_name= ['1','2','3','4','5','6','7']

box_colors = ['blue', 'green', 'pink', 'grey', 'red', 'darkkhaki','darkviolet']

DC1 = [55,55,55,55,60,45,45]
DC2 = [10, 10, 25, 25]
DC3 = [20, 7.3, 7.3]
DC4 = [45,45]
DC5 = [50]
DC6 = [54,54]
DC7 = [107,107]
line_values_list = [DC1,DC2,DC3,DC4,DC5,DC6,DC7] #Dose constraints

label1 = ['D0.03cc <= 55 Gy','D0.03cc <= 55 Gy','D0.03cc <= 55 Gy','D0.03cc <= 55 Gy','D0.03cc <= 60 Gy','D0.03cc <= 45 Gy','D0.03cc <= 45 Gy']
label2 = ['D0.03cc <= 10 Gy','D0.03cc <= 10 Gy','D_mean <= 25 Gy','D_mean <= 25 Gy']
label3 = ['D_mean <= 20 Gy','D40% <= 7.3 Gy','D40% <= 7.3 Gy']
label4 = ['D_mean <= 45 Gy','D_mean <= 45 Gy']
label5 = ['D2% <= 50 Gy']
label6 = ['DOSE CONSTRAINTS:',' Usikker, burde  være [Gy(RBE)]?']
label7 = ['D2% <= 107 Gy','D2% <= 107 Gy']
labels = [label1,label2,label3,label4,label5,label6,label7]


ylabels = ['Dose [Gy(RBE)]','Dose [Gy(RBE)]','Dose [Gy(RBE)]','Dose [Gy(RBE)]','Dose [Gy(RBE)]','Dose [Gy(RBE)]','% of prescribed dose']
pos = ['upper right','best','best','best','right','best','best']
# Gå gjennom hver ROI-gruppe
for idx, ROIs_group in enumerate(ROIs):
    # Liste for å lagre D50-verdier for hver ROI-gruppe
    RBE11_values = []
    RBE_Rorvik_values = []
    RBE11_average = []
    RBE_Rorvik_average = []

    # Gå gjennom hver ROI i gruppen
    for ROI in ROIs_group:
        rbe11 = find_Dose(excel_filbane, ROI)
        RBE11_values.append(rbe11)  # Legg til D50-verdiene for ROI i gruppen
        rbe_Rorvik = find_Dose(excel_rorvik,ROI)
        RBE_Rorvik_values.append(rbe_Rorvik)

        RBE11_average.append(np.sum(rbe11)/len(rbe11))
        RBE_Rorvik_average.append(np.sum(rbe_Rorvik)/len(rbe_Rorvik))


    RBE_difference = []
    RBE_ratio = []
    for i, roi in enumerate(ROIs_group):
        rbe_diff = -RBE11_average[i] + RBE_Rorvik_average[i]
        RBE_difference.append(rbe_diff)
        rbe_ratio = RBE_Rorvik_average[i]/RBE11_average[i]
        RBE_ratio.append(rbe_ratio)

        # Legg til teksten
        print(f"RBE forskjellen mellom RBE_Rorvik og RBE1.1 er for organet {roi}: {RBE_difference[i]:.2f} Gy")
        print(f"RBE forholdet mellom RBE_Rorvik og RBE1.1 er for organet {roi}: {RBE_ratio[i]:.4f}")
        print('-------------------------')


        #D1_values.append(D1)
    # Opprett et boxplot for den aktuelle ROI-gruppen

    box_zip = zip(RBE11_values, RBE_Rorvik_values)
    box_total = list(box_zip)


    #save_file = os.path.join('boxplots_LET', f'{ROIs[idx]}_D50.png')
    plt.figure(figsize=(14, 6))  # Opprett en ny figur for hver ROI-gruppe
    positions = range(1, len(ROIs_group) + 1)  # Definer posisjonene for hver boxplot

    # Tilordne en unik farge til hvert boxplot i gruppen
    for j, (data1, data2) in enumerate(box_total):
        positions = [j * 2 + 1, j * 2 + 2]
        plt.boxplot([data1, data2], positions=positions, labels=['RBE1.1', 'RBE_Rorvik'], patch_artist=True,
                    boxprops=dict(facecolor=box_colors[j]))

        if j < len(line_values_list[idx]):  # Sjekk om det er nok verdier i line_values_list for den aktuelle ROI
            line_value = line_values_list[idx][j]
            # Plasser individuelle hlines for hver ROI
            plt.hlines(y=[line_value], xmin=positions[0] - 0.5, xmax=positions[1] + 0.5, linestyle='--',
                       color=box_colors[j], label=f'{labels[idx][j]}')



        text_y = -0.17 * (plt.ylim()[1] - plt.ylim()[0]) # Plasser navnet under hvert boxplot
        #print('text_y=   ', text_y)
        plt.text((positions[0] + positions[1]) / 2, text_y, ROIs_group[j], ha='center', va='bottom', color=box_colors[j], fontsize=10)
        #plt.text(positions[0], plt.ylim()[1] + 0.02 * (plt.ylim()[1] - plt.ylim()[0]), labels[idx][j], ha='left', va='bottom', fontsize=10)

    # Sett navnene på x-aksen
    #plt.xticks(positions, ["" for _ in positions])  # Fjern standard x-akse etiketter

    save_file = os.path.join('boxplots_rbe_compare', f'{file_name[idx]}.png')

    # Lagre plottet
    plt.ylabel(ylabels[idx])
    plt.legend(loc=pos[idx])  # Vis legenden
    plt.title(r'$RBE_{1.1}$ vs $RBE_{Rorvik}$')
    plt.savefig(save_file)
    #plt.show()

print('Gjennomsnittet av alle forholdene til hvert organ blir %.5f' %np.mean(RBE_ratio))


ny_RBE = np.mean(RBE_ratio)*1.1
print('Dette tilsvarer at RBE= %.5f' %ny_RBE)
