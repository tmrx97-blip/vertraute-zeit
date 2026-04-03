import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. DATENGRUNDLAGE (Hier trägst du deine Werte ein)
zeitpunkte = ['T1', 'T2', 'T3', 'T4']

daten_tabellen = {
    "Fragebogen_Items": {
        'Zeitpunkt': zeitpunkte,
        'Item_1_Lust_auf_Menschen': [2, 2, 3, 4],
        'Item_2_Gespräche_führen':  [1, 2, 3, 4],
        'Item_3_Person_kennengelernt':[1, 1, 2, 3],
        'Item_4_Hilfe_bitten':      [1, 2, 2, 3],
        'Item_5_Etwas_zu_geben':    [2, 3, 3, 4],
        'Item_6_Freude_unternehmen':[2, 2, 4, 4],
        'Item_7_Am_Leben_teilnehmen':[1, 2, 3, 4],
        'Item_8_Zukunft_Aktivitäten':[1, 3, 4, 5]
    },
    "Verfassung_und_Wahrnehmung": {
        'Zeitpunkt': zeitpunkte,
        'Emotionale_Verfassung_(1-10)': [3, 4, 6, 7],
        'Einsamkeitserleben_(1-10)':    [8, 7, 5, 3], 
        'Selbstwirksamkeit_(1-5)':      [1, 2, 3, 4],
        'Schlafqualität_(1-10)':        [4, 4, 6, 8],
        'Vorfreude_(1-5)':              [1, 2, 4, 4],
        'Körperwahrnehmung_Schmerz_(1-5)':[4, 4, 3, 2] 
    }
}

# 2. LOGIK-ENGINE (Chefentwickler-Standard)
def generiere_grafik(name, daten):
    df = pd.DataFrame(daten).set_index('Zeitpunkt')
    df_bereinigt = df.copy()
    
    # Bugfix: Negative Parameter für den Trend spiegeln
    negativ_items = ['Einsamkeitserleben_(1-10)', 'Körperwahrnehmung_Schmerz_(1-5)']
    for item in negativ_items:
        if item in df_bereinigt.columns:
            max_val = 10 if "1-10" in item else 5
            df_bereinigt[item] = (max_val + 1) - df_bereinigt[item]

    # Mathematisch korrekter Gesamttrend
    df['GESAMTTREND'] = df_bereinigt.mean(axis=1, numeric_only=True)

    # Visualisierung
    plt.figure(figsize=(12, 7))
    for col in df.columns:
        if col == 'GESAMTTREND':
            plt.plot(df.index, df[col], color='black', linewidth=4, marker='s', label='DURCHSCHNITT (TREND)')
        else:
            plt.plot(df.index, df[col], linestyle='--', alpha=0.5, marker='o', label=col)

    plt.title(f"Trendanalyse: {name.replace('_', ' ')}", fontsize=16)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{name}.png", dpi=150)
    plt.close()

# 3. AUSFÜHRUNG
for name, daten in daten_tabellen.items():
    generiere_grafik(name, daten)
