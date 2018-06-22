import numpy as np
from keras.callbacks import ModelCheckpoint, TensorBoard

from tester.base_tester import BaseTester


class LodeRunnerTester(BaseTester):
    def __init__(self, model, data, config):
        super(LodeRunnerTester, self).__init__(model, data, config)
        self.callbacks = []
        self.loss = []
        self.acc = []
        self.val_loss = []
        self.val_acc = []
        self.init_callbacks()

    def init_callbacks(self):

        self.callbacks.append(
                TensorBoard(
                    log_dir=self.config.tensorboard_log_dir,
                    write_graph=self.config.tensorboard_write_graph,
                )
            )

        if hasattr(self.config,"comet_api_key"):
            from comet_ml import Experiment
            experiment = Experiment(api_key=self.config.comet_api_key, project_name=self.config.exp_name)
            experiment.disable_mp()
            experiment.log_multiple_params(self.config)
            self.callbacks.append(experiment.get_keras_callback())

    def test(self):
        np.set_printoptions(threshold=np.inf)
        x_train = np.array(self.data[0])
        x_train = np.reshape(x_train,(22350,1,10))
        y_train = np.array(self.data[1])
        history = self.model.fit(
            x_train,y_train,
            batch_size=self.config.batch_size,
            epochs=self.config.num_epochs,
            verbose=self.config.verbose_training,
            validation_split=self.config.validation_split,
            callbacks=self.callbacks,
        )
        self.loss.extend(history.history['loss'])
        self.acc.extend(history.history['acc'])
        self.val_loss.extend(history.history['val_loss'])
        self.val_acc.extend(history.history['val_acc'])
