Phase II Clinical Trial ETL Pipeline
This portfolio project demonstrates a clinical data management workflow using Python, SQLite, and Power BI. The objective of this project was to ingest raw demographic and clinical outcome files, clean the records, isolate a specific target cohort using a relational database engine, and visualize the findings to monitor drug safety and efficacy.
Tech Stack
Python (Pandas & SQLite3): Data ingestion, text standardization, missing-value handling, and database connection.
SQL: Relational data merging (INNER JOIN) and conditional data filtering (WHERE).
Power BI: Business intelligence visualization.
Project Workflow

Data Ingestion & Cleaning (Extract & Transform) I started with two raw files: patient_registry.csv (containing patient demographics) and clinical_outcomes.txt (containing trial results and side effects). Using Pandas, I loaded these files, standardized the text casing for location data, and dropped incomplete records where the patient's age was missing.

Relational Querying (Load & Transform) After merging the datasets in Python on the PatientID primary key, I loaded the combined data into a new SQLite database (phase2_trials.db). I wrote a SQL query to:
Apply a WHERE clause (drug_group = 'Treatment' AND Location = 'Pune') to strictly filter the dataset, isolating only the patients in the target cohort for this study.

Export & Visualization The results of the SQL query were read back into Python and exported as a clean final_report.csv file. I then imported this dataset into Power BI to build a dashboard answering three core business questions:
Is there a difference in treatment efficacy between genders? (Visualized using a Clustered Column Chart: X-Axis = Gender, Y-Axis = Average of efficacy_score)
What is the frequency of reported adverse events? (Visualized using a Bar Chart: X-Axis = Count of PatientID, Y-Axis = adverse_events)
Is there a correlation between patient age and treatment efficacy? (Visualized using a Scatter Plot: X-Axis = Age, Y-Axis = efficacy_score)
