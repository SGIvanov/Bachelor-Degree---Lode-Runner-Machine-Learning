from keras.layers import Dense,LSTM, Activation,CuDNNLSTM
from keras.models import Sequential
from keras.utils import plot_model

from models.base_model import BaseModel


class LodeRunnerModel(BaseModel):
    def __init__(self, config):
        super(LodeRunnerModel, self).__init__(config)
        self.build_model()

    def build_model(self):
        self.model = Sequential()
        self.model.add(CuDNNLSTM(64, input_shape=(1, 10)))
        self.model.add(Dense(10))
        self.model.add(Activation('softmax'))

        self.model.compile(
            loss='categorical_crossentropy',
            optimizer=self.config.optimizer,
            metrics=['acc'],
        )
        # plot_model(self.model, to_file='model.png', show_shapes=True)
