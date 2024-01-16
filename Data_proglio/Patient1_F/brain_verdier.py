

'''
import pandas as pd

def finn_verdi_i_excel(filbane, søkestreng):
    # Les Excel-filen inn i en pandas DataFrame
    df = pd.read_excel(filbane)

    # Iterer gjennom alle kolonner for å finne 'Brain' i radene
    for kolonne_navn in df.columns:
        relevant_rad = df[df[kolonne_navn].astype(str).str.contains('Brain', case=False, na=False)]

        # Hvis det er rader som oppfyller kriteriet, returner verdien fra den første kolonnen
        if not relevant_rad.empty:
            ønsket_verdi = relevant_rad.iloc[0][kolonne_navn]
            return ønsket_verdi

    return None

# Eksempel på bruk:
excel_filbane = 'Patient1_Clinical_Goals.csv'
søkestreng = 'Brain'

resultat = finn_verdi_i_excel(excel_filbane, søkestreng)

if resultat is not None:
    print(f"Ønsket verdi: {resultat}")
else:
    print(f"Ingen match funnet for søkestrengen '{søkestreng}'.")
'''
'''
import pandas as pd
import re

def finn_verdier_i_excel(filbane, søkestreng):
    # Les Excel-filen inn i en pandas DataFrame
    df = pd.read_excel(filbane)

    # Opprett en tom liste for å lagre resultatene
    funnede_verdier = []

    # Iterer gjennom alle celler i DataFrame
    for indeks, rad in df.iterrows():
        for celle in rad:
            # Sjekk om søkestrengen er i cellen
            if søkestreng in str(celle):
                # Bruk regex for å finne verdien i den aktuelle cellen
                match = re.search(r'(\d+,\d+)', str(celle))
                if match:
                    ønsket_verdi = match.group(1)
                    funnede_verdier.append(ønsket_verdi)

    return funnede_verdier

# Eksempel på bruk:
excel_filbane = 'Patient1_ClinicGoals.xlsx'
søkestreng = 'Brain'

resultater = finn_verdier_i_excel(excel_filbane, søkestreng)

if resultater:
    print(f"Ønskede verdier: {resultater}")
else:
    print(f"Ingen match funnet for søkestrengen '{søkestreng}'.")
'''
'''
import pandas as pd

def finn_siste_verdi_i_excel(filbane, søkestreng):
    # Les Excel-filen inn i en pandas DataFrame
    df = pd.read_excel(filbane)

    # Opprett en tom liste for å lagre resultatene
    funnede_verdier = []

    # Iterer gjennom alle radene i DataFrame
    for indeks, rad in df.iterrows():
        # Sjekk om søkestrengen er i raden
        if søkestreng in rad.values:
            # Hent ut den siste verdien i raden
            siste_verdi = rad.iloc[-1]
            funnede_verdier.append(siste_verdi)

    return funnede_verdier

# Eksempel på bruk:
excel_filbane = 'Patient1_ClinicGoals.xlsx'
søkestreng = 'Brain'

resultater = finn_siste_verdi_i_excel(excel_filbane, søkestreng)

if resultater:
    print(f"Siste verdier for strengen '{søkestreng}': {resultater}")
else:
    print(f"Ingen match funnet for søkestrengen '{søkestreng}'.")
'''
'''
import pandas as pd

def finn_siste_verdi_i_excel(filbane, søkestreng):
    # Les Excel-filen inn i en pandas DataFrame
    df = pd.read_excel(filbane)

    # Opprett en tom liste for å lagre resultatene
    funnede_verdier = []

    # Iterer gjennom alle radene i DataFrame
    for indeks, rad in df.iterrows():
        # Sjekk om søkestrengen er til stede i raden
        if søkestreng in rad.values:
            # Finn indeksen til søkestrengen
            indeks_søk = list(rad).index(søkestreng)

            # Hent ut den siste verdien i raden etter søkestrengen
            #siste_verdi = rad.iloc[indeks_søk + 1:].iloc[-1]

            # Legg til i resultatlisten
            funnede_verdier.append(indeks_søk)

    return funnede_verdier

# Eksempel på bruk:
excel_filbane = 'finn_D.xlsx'
søkestreng = 'Brain'

resultater = finn_siste_verdi_i_excel(excel_filbane, søkestreng)

if resultater:
    print(f"Siste verdier for strengen '{søkestreng}': {resultater}")
else:
    print(f"Ingen match funnet for søkestrengen '{søkestreng}'.")
'''

import pandas as pd

def finn_siste_verdi_i_excel(filbane, søkestreng):
    # Les Excel-filen inn i en pandas DataFrame
    df = pd.read_excel(filbane, header=None)

    # Opprett en tom liste for å lagre resultatene
    funnede_verdier = []

    # Iterer gjennom alle radene i DataFrame
    for indeks, rad in df.iterrows():
        # Sjekk om søkestrengen er til stede i raden
        if søkestreng in rad.values:
            # Hent ut den siste verdien i raden
            siste_verdi = rad.iloc[-1]

            # Legg til i resultatlisten
            funnede_verdier.append(siste_verdi)

    return funnede_verdier

# Eksempel på bruk:
excel_filbane = 'finn_D.xlsx'  # Erstatt med din filbane
søkestreng = 'Brain'

resultater = finn_siste_verdi_i_excel(excel_filbane, søkestreng)

if resultater:
    print(f"Siste verdier for strengen '{søkestreng}': {resultater}")
else:
    print(f"Ingen match funnet for søkestrengen '{søkestreng}'.")
