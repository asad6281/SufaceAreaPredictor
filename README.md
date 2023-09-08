# Surface Area Predictor

This repository contains an application that predicts the surface area of a cylinder using machine learning model.

## Requirements

- Git (for cloning the repository)

## Getting Started

### 1. Clone the Repository

If you're accessing this project through GitHub:

` (https://github.com/asad6281/SufaceAreaPredictor.git) `

###2. Make your virtual environment using requirements.txt file using the following command

    - 'conda create --name newenv --file requirements.txt'

    - after making the environment, run the command "appAsad.py" 

### 3. Access the Application

     - After writing the above command, open your browser and navigate to:

     ` http://localhost:5000 `


You should see the Flask application running. Enter the radius and height values to get the predicted surface area of a cylinder.


## Models

The application uses polynomial regression model to make predictions:
   
   we also explore various model
	Linear Regression
	Random Forest
	Ridge Regression
	Neural Network

Multiple models has been trained and validated using a dataset. The best-performing model(polynomial regression) is then selected to make predictions in the Flask application.


## Contact

For any inquiries, issues, or suggestions, please open an issue on GitHub.
