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

![image](https://github.com/user-attachments/assets/0252a6f2-c0a3-47ca-b35e-85091ebfd97d)

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

