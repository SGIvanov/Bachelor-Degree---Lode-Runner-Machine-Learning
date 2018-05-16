from keras.layers import Dense,LSTM, Flatten
from keras.models import Sequential

from models.base_model import BaseModel


class LodeRunnerModel(BaseModel):
    def __init__(self, config):
        super(LodeRunnerModel, self).__init__(config)
        self.build_model()

    def build_model(self):
        self.model = Sequential()
        self.model.add(LSTM(200,input_shape=(10,1),batch_size=self.config.batch_size))
        self.model.add(Dense(10, activation='softmax'))

        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer=self.config.optimizer,
            metrics=['acc'],
        )
