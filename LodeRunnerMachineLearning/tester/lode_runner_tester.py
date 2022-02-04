import numpy as np

from tester.base_tester import BaseTester


class LodeRunnerTester(BaseTester):
    def __init__(self, model, data, config):
        super(LodeRunnerTester, self).__init__(model, data, config)
        self.callbacks = []
        self.loss = 0
        self.acc = 0

    def test(self):
        np.set_printoptions(threshold=np.inf)
        x_test = np.array(self.data[0])
        x_test = np.reshape(x_test,(22350,1,10))
        y_test = np.array(self.data[1])
        history = self.model.evaluate(
            x_test,y_test,
            batch_size=self.config.batch_size,
            verbose=self.config.verbose_training
        )
        self.loss = history[0]
        self.acc = history[1]
        print("Loss :" + str(self.loss))
        print("Accuracy: " +str(self.acc))
