from data_loader.lode_runner_data_loader import LodeRunnerDataLoader
from models.lode_runner_model import LodeRunnerModel
from tester.lode_runner_tester import LodeRunnerTester
from trainers.lode_runner_trainer import LodeRunnerTrainer
from utils.config import process_config
from utils.dirs import create_dirs
from utils.utils import get_args
from keras.models import load_model
import numpy as np


def main():
    try:
        args = get_args()
        config = process_config(args.config)
    except Exception as e:
        print('Failed to upload configurations: '+ str(e))
        exit(0)

    print('Creating new directories...', end='   ')
    create_dirs([config.tensorboard_log_dir, config.checkpoint_dir])
    print('Done')

    data_loader = LodeRunnerDataLoader(config)

    print('Creating the model...', end='   ')
    model = LodeRunnerModel(config)
    print('Done')

    print('Creating the trainer...', end='   ')
    trainer = LodeRunnerTrainer(model.model, data_loader.get_train_data(), config)
    print('Done')

    print('Training the model...', end='   ')
    trainer.train()
    print('Done')

    print('Creating the tester...', end='   ')
    tester = LodeRunnerTester(model.model, data_loader.get_test_data(), config)
    print('Done')

    print('Testing the model...', end='   ')
    tester.test()
    print('Done')

if __name__ == '__main__':
    main()

