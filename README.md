# Diabetes Prediction using Machine Learning

This project utilizes machine learning techniques to predict whether a person has diabetes or not based on certain features. The model is implemented using Flask, a Python web framework, to create a simple web application.

## Files Included

1. `app.py`: This file contains the Flask application code for serving the web application.
2. `diabetes.pkl`: This file contains the trained machine learning model serialized using pickle.
3. `diabetes.csv`: Dataset containing features and outcomes (whether a person has diabetes or not).
4. `templates` directory:
    - `home.html`: HTML template for the home page.
    - `diabetes.html`: HTML template for the diabetes prediction page.

## Setup and Installation

1. Clone this repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Install the required Python packages. You can do this by running:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open a web browser and go to `http://localhost:5000` to access the application.

## Usage

1. **Home Page**: Upon accessing the application, you'll be directed to the home page where you can learn about the project.
2. **Diabetes Prediction Page**: Navigate to the "Diabetes" page using the link provided. Here, you'll be prompted to input certain features related to diabetes.
3. **Prediction**: After entering the required features and submitting the form, the application will display the prediction result, indicating whether the person is likely to have diabetes or not.

## Model Training

The machine learning model used for prediction is a Support Vector Machine (SVM) classifier with a linear kernel. The model was trained using the `diabetes.csv` dataset. The dataset was split into training and testing sets with a ratio of 80:20. After training, the model was serialized using pickle and saved as `diabetes.pkl`.

## Dependencies

- Flask
- numpy
- pandas
- scikit-learn

## Note

- This application provides a simple demonstration of using machine learning for diabetes prediction and should not be used for medical diagnosis purposes.
- Ensure that the required files (`diabetes.pkl`, `diabetes.csv`) are present in the same directory as the Flask application (`app.py`).

## References

- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- scikit-learn Documentation: [https://scikit-learn.org/stable/documentation.html](https://scikit-learn.org/stable/documentation.html)




![image](https://github.com/vaishhnaviis/Diabetes-Prediction-using-ML/assets/77488744/f74fdf96-76bc-4536-9316-9572b0c9a7a0)
