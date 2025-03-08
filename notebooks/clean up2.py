import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the DM Group dataset
dm_df = pd.read_excel("C:/Users/harsh/Medical_Thermogram_Analysis/data/DM_Thermogram_Database.xlsx")

# Check missing values
print(dm_df.isna().sum())

# Fill missing numeric values with median
dm_df.fillna(dm_df.median(numeric_only=True), inplace=True)

# Check for any remaining NaNs
print(dm_df.isna().sum())

# Handle 'Gender' column
dm_df['Gender'] = dm_df['Gender'].replace('Unknown', 'Other')
label_encoder = LabelEncoder()
dm_df['Gender'] = label_encoder.fit_transform(dm_df['Gender'])

# Encode 'Diabetes_Status'
dm_df['Diabetes_Status'] = label_encoder.fit_transform(dm_df['Diabetes_Status'])

# Select numeric columns only
numeric_cols = dm_df.select_dtypes(include=['number']).columns
X = dm_df[numeric_cols]

# Remove any columns still with NaNs
X = X.dropna(axis=1)

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Target variable
y = dm_df['Diabetes_Status']

print("Final check on NaNs:", pd.DataFrame(X).isna().sum().sum())
print("Data cleaned and ready for model training!")
