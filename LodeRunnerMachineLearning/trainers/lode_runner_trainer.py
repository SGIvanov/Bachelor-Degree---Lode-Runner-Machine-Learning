import os
import numpy as np
from keras.callbacks import ModelCheckpoint, TensorBoard
from trainers.base_trainer import BaseTrainer


class LodeRunnerTrainer(BaseTrainer):
    def __init__(self, model, data, config):
        super(LodeRunnerTrainer, self).__init__(model, data, config)
        self.callbacks = []
        self.loss = []
        self.acc = []
        self.val_loss = []
        self.val_acc = []
        self.init_callbacks()

    def init_callbacks(self):
        self.callbacks.append(
            ModelCheckpoint(
                filepath=os.path.join(self.config.checkpoint_dir,
                                      '%s-{epoch:02d}-{val_loss:.2f}.hdf5' % self.config.exp_name),
                monitor=self.config.checkpoint_monitor,
                mode=self.config.checkpoint_mode,
                save_best_only=self.config.checkpoint_save_best_only,
                save_weights_only=self.config.checkpoint_save_weights_only,
                verbose=self.config.checkpoint_verbose,
            )
        )

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

    def train(self):
        np.set_printoptions(threshold=np.inf)
        x_train = np.array(self.data[0])
        x_train = np.reshape(x_train,(44700,1,10))
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
