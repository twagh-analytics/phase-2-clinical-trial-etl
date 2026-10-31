# Phase II Clinical Trial ETL Pipeline 🏥📊

## Project Overview
I built this end-to-end Extract, Transform, and Load (ETL) pipeline to handle messy clinical trial data. The goal of this project is to take raw patient demographics and clinical outcomes, clean them up, merge them, and isolate the exact data we need (specifically, patients in Pune who received the active treatment). This allows us to easily track how well the trial drug worked and monitor any side effects.

## Tools & Tech Stack 🛠️
* **Python (Pandas):** Used for reading the raw files, fixing text errors, dropping blanks, and joining the datasets.
* **SQL (SQLite3):** Used to build the local database and run the exact queries needed to filter our target patient group.
* **Power BI:** Used to build the final interactive dashboard for visual reporting.

## The Data 📁
I worked with two raw files for this project:
1. `patient_registry.csv`: Contains the demographic details (`PatientID`, `Age`, `Gender`, `Location`).
2. `clinical_outcomes.txt`: A tab-separated file with the actual trial results (`PatientID`, `drug_group`, `efficacy_score`, `adverse_events`).

## How I Built It (The ETL Process) ⚙️

### 1. Extract & Transform (Python/Pandas)
* **Data Ingestion:** Loaded both the CSV and TXT files into Pandas dataframes.
* **Cleaning Text:** The location data was messy (e.g., entering "PUNE", "pune", or "Pune"). I standardized everything to Title Case so the database wouldn't get confused during filtering.
* **Handling Blanks:** Dropped any rows where the patient's `Age` was missing to make sure our final analysis was accurate.
* **Merging:** Used an inner join on `PatientID` to combine the demographics and clinical outcomes into one master dataset.

### 2. Load (SQLite)
* Created a local SQLite database (`phase2_trials.db`).
* Pushed the clean master dataframe directly into a new SQL table called `phase2_trials`.

### 3. Query & Export (SQL)
* Wrote a SQL query to filter the database, pulling *only* the patients who were in the 'Treatment' group and located in 'Pune'.
* Exported this final, filtered dataset as `final_report.csv` to feed into Power BI.

## Power BI Dashboard 📈
I loaded the `final_report.csv` into Power BI and built a three-part dashboard (you can view `clinical_dashboard.png` in the repo files above). The dashboard tracks:
* **Efficacy by Gender:** A clustered column chart comparing the average efficacy scores between male and female patients.
* **Adverse Events:** A bar chart showing how many patients reported specific side effects (like Nausea or Fatigue) so we can monitor drug safety.
* **Age vs. Efficacy:** A scatter plot to see if a patient's age had any impact on how well the treatment worked.

## How to Run This Project 🚀
If you want to run this pipeline on your own machine:
1. Make sure you have Python installed, along with the `pandas` library.
2. Clone this repository and make sure the raw data files are in the same folder.
3. Run the script from your terminal:
   ```bash
   python "Phase 2 Clinical Trial.py"
