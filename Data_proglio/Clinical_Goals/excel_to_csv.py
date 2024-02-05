import pandas as pd

# Les data fra Excel-filen
excel_file_path = 'Clinical_Golals_for_all_patients.xlsx'  # Erstatt med stien til din Excel-fil
dataframe = pd.read_excel(excel_file_path)

# Skriv data til en tekstfil (f.eks. CSV)
txt_file_path = 'Clinical_Golals_for_all_patients.txt'  # Stien til den resulterende tekstfilen
dataframe.to_csv(txt_file_path, index=False, sep='\t')
