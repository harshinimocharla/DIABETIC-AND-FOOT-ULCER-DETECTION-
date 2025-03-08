import os
import pandas as pd
import numpy as np

# Paths
dm_group_path = "C:/Users/harsh/Medical_Thermogram_Analysis/data/DM_Group"
output_path = "C:/Users/harsh/Medical_Thermogram_Analysis/data/DM_Thermogram_Database.xlsx"

# List to hold patient data
data = []

# Loop through DM Group folders
for patient_folder in os.listdir(dm_group_path):
    patient_path = os.path.join(dm_group_path, patient_folder)
    if os.path.isdir(patient_path):
        # Extract patient info from folder name
        subject_id = patient_folder

        # Placeholder for actual patient-level metadata (if available)
        # If this exists in separate files, we can read them here
        # For now, we’ll assume placeholders
        gender = 'Unknown'
        age = np.nan
        weight = np.nan
        height = np.nan

        # Extract temperature features from images if available
        left_foot_temp = []
        right_foot_temp = []

        for angiosome in ['Left_Foot', 'Right_Foot']:
            angiosome_path = os.path.join(patient_path, 'Angiosoms', angiosome)
            if os.path.exists(angiosome_path):
                for image_file in os.listdir(angiosome_path):
                    # Placeholder: Actual image processing would go here
                    # For now, we simulate temperature readings
                    temp = np.random.uniform(25, 35)  # Simulated temp value
                    if 'Left' in angiosome:
                        left_foot_temp.append(temp)
                    else:
                        right_foot_temp.append(temp)

        # Calculate temperature features
        left_foot_mean = np.mean(left_foot_temp) if left_foot_temp else np.nan
        right_foot_mean = np.mean(right_foot_temp) if right_foot_temp else np.nan
        temp_difference = right_foot_mean - left_foot_mean

        # Placeholder for ulcer detection based on image anomalies or wound data
        ulcer_presence = 1 if 'Wound_Images' in os.listdir(patient_path) else 0

        # Append data
        data.append([subject_id, gender, age, weight, height, 1, right_foot_mean, left_foot_mean,
                     temp_difference, np.mean([weight / (height ** 2)]) if height else np.nan,
                     np.mean([right_foot_mean, left_foot_mean]),
                     np.var([right_foot_mean, left_foot_mean]),
                     abs(temp_difference), ulcer_presence])

# Create DataFrame
columns = ['Subject', 'Gender', 'Age (years)', 'Weight (Kg)', 'Height (m)', 'Diabetes_Status',
           'RIGHT FOOT', 'LEFT FOOT', 'Temp_Difference', 'IMC', 'Foot_Temp_Mean',
           'Foot_Temp_Variance', 'Foot_Temp_Range', 'Ulcer_Presence']

dm_df = pd.DataFrame(data, columns=columns)

# Save to Excel
dm_df.to_excel(output_path, index=False)
print(f"DM Group data saved to {output_path}")
