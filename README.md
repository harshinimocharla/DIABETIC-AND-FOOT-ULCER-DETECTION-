# Medical Thermal Radiation Image Diagnosis Project

## Project Overview
This project focuses on the diagnosis and monitoring of type 2 diabetes and foot ulcers using deep learning techniques on medical thermal radiation images. The system analyzes plantar thermograms, detects diabetes, identifies foot ulcers, and provides personalized exercise recommendations for diabetic patients.

## Objectives
- **Diabetes Detection:** Classify patients as diabetic or non-diabetic based on plantar thermogram data.
- **Foot Ulcer Detection:** Identify potential foot ulcers in diabetic patients using thermal image analysis.
- **Personalized Exercise Recommendations:** Suggest tailored exercise plans based on patient health data.
- **Remote Monitoring Dashboard:** Provide a user-friendly dashboard for healthcare professionals to track patient progress and health.

## Project Structure
Medical_Thermogram_Analysis/
│
├── data/                                        # Raw and processed data
│   ├── Control_Group/                           # Healthy patients
│   ├── DM_Group/                                # Diabetic patients
│   ├── Plantar_Thermogram_Database.xlsx         # Metadata and patient info
│   ├── engineered_features.xlsx                 # Processed feature data
│
├── DFU_Dataset/                                 # Diabetic Foot Ulcer dataset
│   ├── Transfer_Learning_Images/                
│   │   ├── Sample/                              
│   │   ├── Internet_Set/                        
│   │   ├── Wound_Images_2/                      
│   │   ├── Wound_Images/                        
│   │
│   ├── Test_Set/                                
│   │   ├── Images/                              
│   │
│   ├── Patches/                                
│   │   ├── Normal/                              # Healthy skin patches
│   │   ├── Abnormal/                            # Ulcerated skin patches
│   │
│   ├── Original_Images/                        
│
├── src/                                         # Source code
│   ├── data_processing/                         # Data loading and preprocessing
│   │   ├── preprocess.py                        
│   │   ├── feature_engineering.py               
│   │
│   ├── models/                                  # Model architectures
│   │   ├── cnn_diabetes_model.py                
│   │   ├── cnn_ulcer_detection_model.py         
│   │
│   ├── utils/                                   # Helper functions
│   │   ├── visualization.py                     
│   │   ├── metrics.py                           
│   │
│   ├── deployment/                              # Deployment scripts
│   │   ├── web_app.py                            # Simple web app for predictions
│   │   ├── dashboard.py                          # Remote monitoring dashboard
│
├── Models/                                      # Saved models and checkpoints
│   ├── Diabetes_Detection_Model/                
│   ├── Foot_Ulcer_Detection_Model/              
│
├── Notebooks/                                   # Jupyter notebooks
│   ├── 01_Data_Preprocessing.ipynb              
│   ├── 02_EDA.ipynb                             
│   ├── 03_Feature_Engineering.ipynb             
│   ├── 04_Model_Training.ipynb                  
│   ├── 05_Deployment.ipynb                      
│
├── Web_App/                                     # Simple prediction interface
│
├── Dashboard/                                   # Remote monitoring & exercise recommendations
│
├── Results/                                     # Model results and analysis
│
├── templates/                                   # Frontend templates
│
├── README.md                                    # Project documentation
├── roadmap.md                                   # Project plan and progress tracking
├── requirements.txt                             # Libraries and dependencies
└── .gitignore                                   # Ignored files for version control

## Data Description
- **Plantar_Thermogram_Database.xlsx:** Complete patient records with demographic, clinical, and temperature data.
- **Enhanced_Plantar_Thermogram_Database.xlsx:** Feature-engineered dataset with temperature differences, IMC categories, and statistical features.
- **DFU_Dataset:** Contains foot ulcer images and patches categorized into normal and abnormal.

## Dataset Links
- **Foot Ulcer Detection Dataset:** [Kaggle DFU Dataset](https://www.kaggle.com/datasets/laithjj/diabetic-foot-ulcer-dfu/data)
- **Type 2 Diabetes Dataset:** [IEEE Dataport](https://ieee-dataport.org/documents/type-2-diabetes-dataset)

## Feature Engineering
- **Temperature Differences:** Difference between left and right foot temperatures.
- **IMC Categories:** BMI categorized into underweight, normal, overweight, and obese.
- **Statistical Features:** Mean, variance, and range of foot temperatures.
- **Temperature Anomalies:** Highlighting asymmetry and potential early ulcer signs.

## Model Training
- **Diabetes Detection Model:** CNN achieving 100% accuracy on the enhanced dataset.
- **Foot Ulcer Detection Model:** CNN fine-tuned for multi-class classification of ulcer stages.

## Deployment
- **Simple Web App:** For patient-level predictions.
- **Advanced Dashboard:** For remote monitoring, data visualization, and exercise recommendations.

## How to Run
1. **Set up the environment:**
```bash
pip install -r requirements.txt
```
2. **Train the models:**
Run the model training notebooks or scripts.
3. **Deploy the web app:**
Run the deployment notebook or server script.

## Future Work
- Integrate real-time monitoring.
- Expand exercise recommendation system.
- Enhance foot ulcer detection accuracy.

## Contributors
- **Your Name** - Project Lead

## Acknowledgments
Special thanks to the researchers and datasets that made this project possible.

