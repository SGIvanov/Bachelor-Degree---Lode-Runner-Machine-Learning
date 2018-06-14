import string

import numpy as np
from keras.models import load_model
import os


def main():
    dir_name = os.path.dirname(__file__)
    model_file = os.path.join(dir_name, 'selectedModels/LodeRunner_LSTM-01-1.27.hdf5')
    model = load_model(model_file)
    vector = start_vector(True, 0)
    map = np.chararray((16, 28), unicode=True)
    map[:] = ' '
    sign = 1
    for j in range(0, 28):
        if sign:
            start = 0
            end = 16
            step = 1
        else:
            start = 15
            end = -1
            step = -1
        for i in range(start, end,step):
            prediction = model.predict(vector)
            vector = predict_next(prediction[0])
            map[i][j] = map_elements(vector[0][0])
        sign = abs(sign - 1)
    for i in range(0, 16):
        for j in range(0, 28):
            if map[i][j] == '':
                print(" ", end='')
            print(map[i][j], end='')


def predict_next(prediction):
    random = np.random.rand()
    j = 0.0
    for i in range(0, 10):
        j += prediction[i]
        if random <= j:
            break
    return start_vector(False, i)


def map_elements(vector):
    if np.array_equal(vector, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
        return '#'
    elif np.array_equal(vector, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]):
        return '@'
    elif np.array_equal(vector, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]):
        return 'H'
    elif np.array_equal(vector, [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]):
        return '-'
    elif np.array_equal(vector, [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]):
        return 'X'
    elif np.array_equal(vector, [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]):
        return 'S'
    elif np.array_equal(vector, [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]):
        return '$'
    elif np.array_equal(vector, [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]):
        return '0'
    elif np.array_equal(vector, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]):
        return '&'
    else:
        return ''

def start_vector(total_random,position):
    start = np.zeros(10)
    if total_random:
        random = np.random.randint(10)
        start = np.zeros(10)
        start[random] = 1
    else:
        start[position] = 1
    vector = start.reshape(1, 1, 10)
    return vector


def mock_map():
    level="                  S         " +\
        "    $             S         " +\
        "#######H#######   S         " +\
        "       H----------S    $    " +\
        "       H    ##H   #######H##" +\
        "       H    ##H          H  " +\
        "     0 H    ##H       $0 H  " +\
        "##H#####    ########H#######" +\
        "  H                 H       " +\
        "  H           0     H       " +\
        "#########H##########H       " +\
        "         H          H       " +\
        "       $ H----------H   $   " +\
        "    H######         #######H" +\
        "    H         &  $ $$      H" +\
        "############################"
    return level


if __name__ == '__main__':
    main()