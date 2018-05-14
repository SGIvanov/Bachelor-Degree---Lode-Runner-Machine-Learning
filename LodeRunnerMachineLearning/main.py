from data_loader.simple_mnist_data_loader import SimpleMnistDataLoader
from models.simple_mnist_model import SimpleMnistModel
from trainers.simple_mnist_trainer import SimpleMnistModelTrainer
from utils.config import process_config
from utils.dirs import create_dirs
from utils.utils import get_args


def main():
    try:
        args = get_args()
        config = process_config(args.config)
    except Exception as e:
        print('Failed to upload configurations: '+ str(e))
        exit(0)

    print('Creating new directories...',end = '   ')
    create_dirs([config.tensorboard_log_dir, config.checkpoint_dir])
    print('Done')

    print('Loading training and test data...',end = '   ')
    data_loader = SimpleMnistDataLoader(config)
    print('Done')

    print('Creating the model...',end = '   ')
    model = SimpleMnistModel(config)
    print('Done')

    print('Creating the trainer...',end = '   ')
    trainer = SimpleMnistModelTrainer(model.model, data_loader.get_train_data(), config)
    print('Done')

    print('Training the model...', end = '   ')
    trainer.train()
    print('Done')


if __name__ == '__main__':
    main()
