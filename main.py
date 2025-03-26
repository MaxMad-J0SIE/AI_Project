import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from data_holder import DataHolder

data_holder = DataHolder()

class Main:
    full_data = data_holder.tesla_stocked_full
    short_data = data_holder.tesla_stock

    train_data = full_data[:-5]
    test_data = full_data[-5:]

    X_train = train_data[:-1, :-1]
    y_train = train_data[1:, 3]

    X_test = test_data[:-1, :-1]
    y_test = test_data[1:, 3]

    print("Training Features (X_train) shape:", X_train.shape)
    print("Training Target (y_train) shape:", y_train.shape)
    print("Testing Features (X_test) shape:", X_test.shape)
    print("Testing Target (y_test) shape:", y_test.shape)

    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Reshape y_train and y_test to be 2D arrays as expected by some loss functions
    y_train = y_train.reshape(-1, 1)
    y_test = y_test.reshape(-1, 1)

    # Define the model using the Keras Sequential API
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),  # Input shape is 4 features
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)  # Output layer with 1 neuron for the predicted closing price
    ])