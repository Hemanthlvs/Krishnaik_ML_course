# Krishnaik_ML_course

## This is an end to end datascience project.

## setup.py
The setup.py file is essential for packaging and distributing your Python project. It contains key information about your project, such as its name, version, and author. This file allows others to easily install your project using package managers like pip.
### Use:
Easy Installation: Users can install your project with a simple command, making it accessible to others.
Dependency Management: It helps specify any external libraries your project needs, ensuring users have everything required to run your code.


## .gitignore
The .gitignore file is used to specify which files or directories Git should ignore when you commit your code. This is particularly useful for excluding files that are not necessary for your project, such as temporary files, logs, or sensitive information.
### Use:
Cleaner Repositories: By ignoring unnecessary files, your repository remains clean and focused on the important code.
Security: It helps prevent sensitive information (like API keys or passwords) from being accidentally shared in the repository.


## requirements.txt
The requirements.txt file lists all the external packages that your project depends on. This file allows others to quickly install the necessary packages using a single command.
### Use:
Simplified Setup: New users can set up your project environment easily by installing all required packages at once.
Version Control: By specifying package versions, it ensures that everyone uses the same versions, reducing compatibility issues and bugs.


## Artifacts Folder
The artifacts folder contains important files created by the machine learning scripts.
### Contents:
**raw_data.csv**: Original datasets used for training and testing.

**test_data.csv**: Datasets for evaluating model performance.

**train_data.csv**: Datasets used to train the models.

**transformed.pkl**: Processed data ready for training.

**model.pkl**: The trained machine learning model.

These files are essential for running and understanding the machine learning projects.

## Components Overview :
The src/components folder contains scripts responsible for data ingestion, transformation, and model training in the machine learning pipeline.
**1. data_ingestion.py**
This script handles the ingestion of raw data. It performs the following tasks:
- Reads the raw data from a CSV file.
- Creates an artifacts folder to store processed data.
- Splits the data into training and testing sets.
- Saves the raw, training, and testing datasets as CSV files in the artifacts folder.

**2. data_transformer.py**
This script is responsible for transforming the ingested data. It includes:
- Reading the training and testing datasets.
- Applying preprocessing steps such as imputation and scaling for numeric and categorical features.
- Standardizing the data and saving the transformation object as a pickle file for future use.
  
**3. model_training.py**
This script focuses on training various machine learning models. It performs the following:
- Initializes and trains multiple regression models.
- Evaluates the models using R² scores to determine their performance.
- Saves the best-performing model as a pickle file for deployment.

## Pipelines Overview
The src/pipelines folder contains scripts that facilitate the prediction process using the trained machine learning model.

**predict_pipeline.py**
This script is responsible for making predictions based on new input data. It includes the following components:

**1. pred_pipeline Class**
  **Initialization:** Sets up the prediction pipeline.
  **predict Method:**
  - Loads the transformation object and the trained model from the artifacts folder.
  - Transforms the input features using the loaded transformer.
  - Makes predictions using the trained model and returns the predicted values.
    
**2. CustomData Class**
  **Initialization:** Accepts various input features such as gender, race/ethnicity, parental education level, lunch status, test preparation course, reading score, and writing score.
  **get_data_as_data_frame Method:**
  Converts the input features into a Pandas DataFrame format, which can be used for making predictions.
