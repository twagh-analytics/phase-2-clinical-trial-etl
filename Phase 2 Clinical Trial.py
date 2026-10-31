
import pandas as pd
import sqlite3

df_patient = pd.read_csv("patient_registry.csv")
df_clinical = pd.read_csv("clinical_outcomes.txt", sep="\t")

df_patient['Location'] = df_patient['Location'].str.replace("PUNE", "pune").str.replace("pune", "Pune")
df_patient = df_patient.dropna(subset='Age')
df_master = pd.merge(df_patient, df_clinical, on='PatientID')
conn = sqlite3.connect('phase2_trials.db')
df_master.to_sql('phase2_trials', conn, if_exists='replace', index=False)

sql_query = '''
SELECT * 
FROM phase2_trials
WHERE drug_group = 'Treatment' AND Location = 'Pune';  '''

df_final_report = pd.read_sql_query(sql_query, conn)
df_final_report.to_csv('final_report.csv', index=False)
conn.close()

print("Files 'final_report.csv' generated successfully.")



