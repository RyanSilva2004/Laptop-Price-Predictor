# Laptop Price Predictor

## Overview
This repository contains a Python machine learning model for predicting laptop prices. The model is deployed using a Flask server.

![ezgif-4-844b93b998](https://github.com/RyanSilva2004/Laptop-Price-Predictor/assets/137909008/818c25fb-9d74-4298-87e8-137193029317)


## Features
The model takes into account various features of a laptop to predict its price. These features include but are not limited to:
- Brand
- Type of Processor
- RAM
- Screen Technology
- Operating System
- Graphics Card
- Weight

## Installation & Setup
Follow these steps to get the project up and running on your local machine:

1. **Clone the repository**
    ```
    git clone https://github.com/RyanSilva2004/Laptop-Price-Predictor.git
    ```
2. **Navigate to the project directory**
    ```
    cd Laptop-Price-Predictor
    ```
3. **Install the required Python packages**
    ```
    pip install -r requirements.txt
    ```
4. **Run the Flask server**
    ```
    python app.py
    ```
Now, you should be able to access the application on your local machine at `http://localhost:5000`.

## Usage
Once the server is running, you can input the features of the laptop for which you want to predict the price. The application will return the predicted price based on the trained machine learning model.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

