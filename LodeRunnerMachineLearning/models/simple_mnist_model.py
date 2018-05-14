from keras.layers import Dense
from keras.models import Sequential

from models.base_model import BaseModel


class SimpleMnistModel(BaseModel):
    def __init__(self, config):
        super(SimpleMnistModel, self).__init__(config)
        self.build_model()

    def build_model(self):
        self.model = Sequential()
        self.model.add(Dense(32, activation='relu', input_shape=(28 * 28,)))
        self.model.add(Dense(16, activation='relu'))
        self.model.add(Dense(10, activation='softmax'))

        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer=self.config.optimizer,
            metrics=['acc'],
        )
