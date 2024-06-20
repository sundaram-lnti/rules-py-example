import numpy as np
import tensorflow as tf


class FashionMnist:
    def __init__(self):
        (X_train_full, y_train_full), (X_test_full, y_test_full) = tf.keras.datasets.fashion_mnist.load_data()
        self.X_train, self.y_train = X_train_full, y_train_full
        self.X_test, self.y_test = X_test_full, y_test_full

    def get_train_dataset(self) -> tuple[np.ndarray, np.ndarray]:
        return self.X_train, self.y_train

    def get_test_dataset(self) -> tuple[np.ndarray, np.ndarray]:
        print(self.X_test.shape)
        return self.X_test, self.y_test

if __name__ == "__main__":
    print(type(FashionMnist().get_test_dataset()))
