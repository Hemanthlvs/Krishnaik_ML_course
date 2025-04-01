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

## src/exception.py
This script defines custom exception handling for the project, providing detailed error messages to aid in debugging.

**Key Components:**
1. error_msg_detail Function
This function takes an error and its details as input.
It extracts the filename and line number where the error occurred.
It formats and returns a detailed error message, including the script name, line number, and the error message itself.
2. CustomException Class
Inherits from the built-in Exception class.
Initializes with an error message and error details.
Calls the error_msg_detail function to generate a detailed error message.
Overrides the __str__ method to return the custom error message when the exception is printed.
3. Testing (Commented Out)
The script includes a commented-out section that demonstrates how to raise a CustomException by intentionally causing a ZeroDivisionError.


## src/logger.py 
This script sets up a logging mechanism for the project, allowing for the tracking of events and errors during execution.

**Key Components:**
1. Log File Creation
The script generates a log file with a timestamp in the format MM_DD_YY_HH_MM_SS.log.
It creates a directory named Logs in the current working directory to store the log files.
2. Logging Configuration
The logging.basicConfig function is used to configure the logging settings:
Filename: Specifies the path to the log file.
Format: Defines the format of the log messages, including the timestamp, line number, logger name, log level, and the actual message.
Level: Sets the logging level to INFO, meaning that all messages at this level and above will be recorded.
3. Example Logging
An example log message ("Logging has started.") is recorded to demonstrate the logging functionality.


## src/utils.py 
script contains utility functions for saving and loading objects, as well as evaluating machine learning models.

**Key Components:**
1. save_obj Function
This function saves a Python object to a specified file path using the dill library.
It ensures that the directory for the file path exists, creating it if necessary.
If an error occurs during the saving process, it raises a CustomException.
2. load_path Function
This function loads a Python object from a specified file path using the dill library.
It opens the file in read-binary mode and returns the loaded object.
If an error occurs during the loading process, it raises a CustomException with the error details.
3. (Commented Out) evaluate_model Function
This function, currently commented out, is intended to evaluate multiple machine learning models.
It would fit each model to the training data, make predictions, and calculate the R² score for both training and testing datasets.
The results would be stored in a report dictionary.


## app.py 
script sets up a Flask web application that allows users to input data and receive predictions from a machine learning model.

**Key Components:**
1. Flask Application Setup
The script imports necessary libraries, including Flask for web development and various data handling libraries.
It initializes the Flask application.
2. Home Route
The @app.route('/') decorator defines the home page route.
The index function renders the index.html template when the home page is accessed.
3. Prediction Route
The @app.route('/predictdata', methods=['GET', 'POST']) decorator defines a route for handling prediction requests.
GET Request: Renders the home.html template for user input.
POST Request:
Collects user input from the form and creates an instance of the CustomData class.
Converts the input data into a DataFrame using the get_data_as_data_frame method.
Initializes the pred_pipeline class and calls the predict method to get predictions.
Renders the home.html template again, displaying the prediction results.
4. Running the Application
The application runs in debug mode on host 0.0.0.0 and port 5000, allowing it to be accessed from any network interface.

## Dockerfile Overview
The Dockerfile is used to create a Docker image for the Flask web application, allowing for easy deployment and consistency across different environments.

**Key Components:**
1. Base Image
FROM python:3.7-slim-buster: Specifies the base image to use, which is a lightweight version of Python 3.7.
2. Working Directory
WORKDIR /app: Sets the working directory inside the container to /app, where the application code will reside.
3. Copying Files
COPY . /app: Copies all files from the current directory on the host machine to the /app directory in the container.
4. Updating Package Lists
RUN apt update -y: Updates the package lists for the APT package manager.
5. Installing Dependencies
RUN apt-get update && pip install -r requirements.txt: Installs the required Python packages listed in the requirements.txt file.
6. Command to Run the Application
CMD ["python3", "app.py"]: Specifies the command to run the application when the container starts, which executes the app.py script.




---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Docker steps run from terminal:

- docker build -t testdockerkrish.azurecr.io/mltest:latest .
- docker login testdockerkrish.azurecr.io
- docker push testdockerkrish.azurecr.io/mltest:latest
