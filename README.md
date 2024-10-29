# Algerian Forest Fire Prediction

This project is a Streamlit application designed to predict the Fire Weather Index (FWI) for Algerian forest fires based on various environmental input parameters. The application uses a Ridge Machine Learning model trained to provide insights into the likelihood of fire occurrences, helping in proactive forest management. The purpose of the project is to provide the end to end project deployment, starting from EDA, Feature Engineerin and Model Training till the automated deployment setup on AWS Elastic Beanstalk using AWS Code Pipeline


## Features

- User-friendly interface for inputting environmental parameters.
- Predicts the Fire Weather Index (FWI) based on user inputs.
- Displays the prediction results clearly.
- Deployed on AWS Elastic Beanstalk with continuous integration through AWS CodePipeline.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Murtuzasaifee/ml_forestfire_prediction.git
    cd ml_forestfire_prediction
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    conda create -p venv python==3.12
    conda activate {YOUR_PATH}
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application locally, use the following command:

```bash
streamlit run app/app.py
  ```

## Input Parameters

The following input parameters are required for predicting the Fire Weather Index (FWI):

| Parameter                        | Description                                                | Input Type        |
|----------------------------------|------------------------------------------------------------|-------------------|
| **Temperature**                  | Air temperature in degrees Celsius (°C)                   | Number (0.0 - 50.0) |
| **Relative Humidity (RH)**       | Percentage of relative humidity                             | Number (0 - 100)   |
| **Wind Speed (Ws)**              | Wind speed in kilometers per hour (km/h)                  | Number (0.0 - 50.0) |
| **Rainfall (Rain)**              | Rainfall amount in millimeters (mm)                        | Number (0.0 - 50.0) |
| **Fine Fuel Moisture Code (FFMC)** | Code representing the moisture content of fine fuels       | Number (0.0 - 100.0) |
| **Duff Moisture Code (DMC)**     | Code representing the moisture content of duff             | Number (0.0 - 100.0) |
| **Initial Spread Index (ISI)**    | Index indicating the potential rate of fire spread         | Number (0.0 - 50.0) |
| **Classes**                       | Select the class: "Fire" or "Not Fire"                    | Dropdown          |
| **Region**                        | Select the region: "Bijaya Region" or "Sidi Bell Region"  | Dropdown          |

After entering the values, click the **Predict** button to see the predicted FWI.


## Project Structure

The project has the following structure:

- algerian-forest-fire-prediction/
    - app/
        - application.py  # Entry point for AWS Elastic Beanstalk
        - app.py          # Streamlit application code
    - requirements.txt     # Required Python packages
    - application_start.sh  # Script to start the application
    - Procfile              # Configuration for AWS Elastic Beanstalk
    - models/               # Folder containing trained models
        - ridge.pkl
        - scaler.pkl


### Description of Key Files

- **`application.py`**: This file serves as the entry point for AWS Elastic Beanstalk, starting the Streamlit application.
- **`app.py`**: Contains the main Streamlit application code, including the user interface and prediction logic.
- **`models/`**: Folder containing the trained machine learning models (Ridge regression and scaler).
- **`requirements.txt`**: Lists the necessary Python packages to run the application.
- **`application_start.sh`**: A shell script used to install dependencies and run the application on Elastic Beanstalk.
- **`Procfile`**: A configuration file that tells Elastic Beanstalk how to run the application.


## Deployment

This Streamlit application can be deployed on AWS Elastic Beanstalk. Ensure you have the AWS CLI set up and configured. The deployment process can be automated using AWS CodePipeline.

#### Steps to Deploy:

1. **Create an Elastic Beanstalk Application**:
   - Log in to the AWS Management Console.
   - Navigate to the Elastic Beanstalk service.
   - Click on **Create Application** and follow the prompts to set it up.

2. **Set Up CodePipeline**:
   - In the AWS Management Console, navigate to the CodePipeline service.
   - Click on **Create pipeline**.
   - Connect your GitHub repository to automate the build and deployment process.

3. **Push Changes to GitHub**:
   - Make any updates or changes to your application code.
   - Push these changes to your GitHub repository.
   - CodePipeline will automatically detect the changes and deploy the updated application to Elastic Beanstalk.

### Notes
- Ensure that all necessary environment variables are configured in the Elastic Beanstalk environment settings.
- Monitor the deployment process through the AWS Management Console for any issues.


## License
This project is licensed under the MIT License - see the LICENSE file for details.