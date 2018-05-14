from keras.datasets import mnist

from data_loader.base_data_loader import BaseDataLoader


class SimpleMnistDataLoader(BaseDataLoader):
    def __init__(self, config):
        super(SimpleMnistDataLoader, self).__init__(config)

    def get_train_data(self):
        return self.X_train, self.y_train

    def get_test_data(self):
        return self.X_test, self.y_test
