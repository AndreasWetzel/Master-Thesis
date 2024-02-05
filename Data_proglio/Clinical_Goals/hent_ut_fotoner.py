import pandas as pd

df = pd.read_excel('Clinical_Golals_for_all_patients.xlsx', header=None)
funnede_verdier = []
pas_nr = []
parameter = []
fotoner = []
ROI = []


for indeks, rad in df.iterrows():
    if rad.iloc[1] == 0:
        dose = rad.iloc[-1]  # Gitt dose
        pas = rad.iloc[0]    # Pasient nummer
        par = rad.iloc[-2]   # Kriterier
        ROI_ = rad.iloc[2]

        pas_nr.append(str(pas))
        funnede_verdier.append(dose)
        parameter.append(par)
        fotoner.append(0)
        ROI.append(ROI_)


# Lag en DataFrame med de oppdaterte listene
result_df = pd.DataFrame({
    "Pasient_nummer": pas_nr,
    "Foton eller proton [0,1]": fotoner,
    "Organ": ROI,
    "Kriterier": parameter,
    "Gitt_dose": funnede_verdier
})


# Skriv DataFrame til en ny Excel-fil
result_filename = "foton_doser.xlsx"
result_df.to_excel(result_filename, index=False)
