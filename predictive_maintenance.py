import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import logging
import joblib
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load dataset from CSV.
    :param file_path: Path to the CSV file
    :return: pandas DataFrame
    """
    if not os.path.exists(file_path):
        logging.error(f"File {file_path} not found.")
        raise FileNotFoundError(f"File {file_path} does not exist.")
    
    try:
        data = pd.read_csv(file_path)
        logging.info("Dataset loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def preprocess_data(data):
    """
    Preprocess data, separate features and labels.
    :param data: pandas DataFrame containing the dataset
    :return: features (X), labels (y)
    """
    try:
        X = data[['temperature', 'vibration', 'pressure', 'airQuality']]
        y = data['maintenance_needed']
        logging.info("Data preprocessing complete.")
        return X, y
    except KeyError as e:
        logging.error(f"Column missing: {e}")
        raise

def train_model(X_train, y_train):
    """
    Train the RandomForest model.
    :param X_train: Training features
    :param y_train: Training labels
    :return: trained model
    """
    model = RandomForestClassifier(random_state=42, n_estimators=100)
    model.fit(X_train, y_train)
    logging.info("Model training complete.")
    return model

def save_model(model, file_path='random_forest_model.pkl'):
    """
    Save the trained model to a file.
    :param model: Trained model
    :param file_path: Path to save the model
    """
    try:
        joblib.dump(model, file_path)
        logging.info(f"Model saved to {file_path}.")
    except Exception as e:
        logging.error(f"Error saving model: {e}")
        raise

def load_model(file_path='random_forest_model.pkl'):
    """
    Load a previously saved model from a file.
    :param file_path: Path to the saved model file
    :return: loaded model
    """
    try:
        model = joblib.load(file_path)
        logging.info(f"Model loaded from {file_path}.")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        raise

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model and print out accuracy and classification report.
    :param model: Trained model
    :param X_test: Test features
    :param y_test: Test labels
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    logging.info(f"Model accuracy: {accuracy * 100:.2f}%")
    logging.info("Classification Report:")
    logging.info("\n" + classification_report(y_test, predictions))

def main():
    # Load and preprocess the dataset
    data = load_data('sensor_data.csv')
    X, y = preprocess_data(data)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Check if a model already exists
    model_file = 'random_forest_model.pkl'
    if os.path.exists(model_file):
        logging.info("Loading existing model...")
        model = load_model(model_file)
    else:
        # Train a new model
        logging.info("Training new model...")
        model = train_model(X_train, y_train)
        save_model(model, model_file)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
