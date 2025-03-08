import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import os
from keras.models import Sequential
from keras.layers import Dense, Input
input_features = ['Age (years)', 'Weight (Kg)', 'Height (m)', 'IMC', 
                  'RIGHT FOOT', 'LEFT FOOT', 'Temp_Difference', 'IMC_Category',
                  'Foot_Temp_Mean', 'Foot_Temp_Variance', 'Foot_Temp_Range', 'Temp_Anomaly']


input_dim = len(input_features)  # The number of features in your dataset

model = Sequential([
    Input(shape=(input_dim,)),        # Define input layer separately
    Dense(64, activation='relu'),     # Hidden layer
    Dense(1, activation='sigmoid')    # Output layer for binary classification
])



# File path to the enhanced data
file_path = 'C:/Users/harsh/Medical_Thermogram_Analysis/data/Enhanced_Plantar_Thermogram_Database.xlsx'

# Check if the file exists
if os.path.exists(file_path):
    print("File exists. Trying to load it...")
    try:
        df = pd.read_excel(file_path)
        print("File loaded successfully!")
        print(df.head())  # Show the first few rows
        print(df.columns) # Show the column names
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
else:
    print(f"File not found at: {file_path}")



# File path to the enhanced data
file_path = 'C:/Users/harsh/Medical_Thermogram_Analysis/data/Enhanced_Plantar_Thermogram_Database.xlsx'

# Load the data
try:
    df = pd.read_excel(file_path)
    print("File loaded successfully!")
    print(df.head())  # Show the first few rows
    print(df.columns) # Show the column names
except FileNotFoundError:
    print(f"File not found at: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")



# Load the enhanced data
data_path = 'C:/Users/harsh/Medical_Thermogram_Analysis/data/Enhanced_Plantar_Thermogram_Database.xlsx'
df = pd.read_excel(data_path)

# Clean the data: Drop rows with NaNs
df.dropna(inplace=True)

# Select features and target
features = ['Age (years)', 'Weight (Kg)', 'Height (m)', 'RIGHT FOOT', 'LEFT FOOT',
            'Temp_Difference', 'IMC', 'Foot_Temp_Mean', 'Foot_Temp_Variance', 'Foot_Temp_Range']
target = 'Diabetes_Status'

X = df[features]
y = df[target]

# Scale the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the CNN model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Save the model

model.save('C:/Users/harsh/Medical_Thermogram_Analysis/models/diabetes_cnn_model.keras')
print("Model training complete and saved!")



