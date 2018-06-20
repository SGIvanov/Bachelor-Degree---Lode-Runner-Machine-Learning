import numpy as np
from keras.models import load_model
import os


def main():
    dir_name = os.path.dirname(__file__)
    model_file = os.path.join(dir_name, 'selectedModels/LodeRunner_LSTM-01-1.27.hdf5')
    np.random.seed(37)
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

    create_first_floor(map)
    ensure_functional_ladder(map)
    fill_too_small_gaps(map)
    clear_second_floor(map)
    ensure_ladder_touch_ground(map)

    ensure_number_of_pickups(map)
    ensure_pickups_touch_ground(map)

    ensure_number_of_enemies(map)

    clear_last_floor(map)

    longer_hand_bars(map)

    ensure_player(map)

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


def ensure_player(map):
    for i in range(0, 16):
        for j in range(0, 28):
            # ensure player not on first line
            if map[i][j] == '&' :
                map[i][j] = ''
    for j in range(0, 28):
        if map[14][j] == '':
            map[14][j] = '&'
            return


def ensure_number_of_pickups(map):
    max_number = 4
    for i in range(15, -1, -1):
        for j in range(0, 28):
            if map[i][j] == '$' and max_number >= 0:
                max_number = max_number - 1
            elif map[i][j] == '$' and max_number < 0:
                map[i][j] = ''


def ensure_number_of_enemies(map):
    max_number = 2
    for i in range(0, 16):
        for j in range(0, 28):
            if map[i][j] == '0' and max_number >= 0:
                max_number = max_number - 1
            elif map[i][j] == '0' and max_number < 0:
                map[i][j] = ''

    if max_number >= 0:
        for i in range(0, 16):
            for j in range(0, 28):
                if map[i][j] == '' and max_number >= 0:
                    map[i][j] = '0'
                    max_number = max_number - 1
                if max_number < 0:
                    return


def create_first_floor(map):
        for j in range(0, 28):
            map[15][j] = '#'


def clear_second_floor(map):
    for j in range(0, 28):
        if map[14][j] == '#' or map[14][j] == '@' or map[14][j] == 'X':
            map[14][j] = ''


def clear_last_floor(map):
    for j in range(0, 28):
        if map[0][j] == '#' or map[14][j] == '@' or map[14][j] == 'X':
            map[0][j] = ''


def ensure_ladder_touch_ground(map):
    for j in range(0, 28):
        for i in range(0, 16):
            if map[i][j] == 'H' and i != 14:
                while map[i+1][j] != '@' and map[i+1][j] != 'X' and map[i+1][j] != '#':
                    map[i + 1][j] = 'H'
                    i = i + 1


def ensure_pickups_touch_ground(map):
    for j in range(0, 28):
        for i in range(0, 16):
            if map[i][j] == '$':
                map[i][j] = ''
                while map[i+1][j] != '@' and map[i+1][j] != '#' and map[i+1][j] != 'H':
                    i = i + 1
                map[i][j] = '$'


def longer_hand_bars(map):
    for i in range(0, 16):
        for j in range(0, 28):
            if map[i][j] == '-':
                if j+1 <= 27 and map[i][j + 1] == '':
                    map[i][j + 1] = '-'
        for j in range(27, -1,-1):
            if map[i][j] == '-':
                if j-1 >= 0 and map[i][j - 1] == '':
                    map[i][j - 1] = '-'


def ensure_functional_ladder(map):
    for i in range(0, 16):
        for j in range(0, 28):
            if i != 0:
                if map[i][j] == 'H' and map[i - 1][j] == 'H':
                    if j-1 >= 0:
                        map[i][j-1] = ''
                    if j + 1 <= 27:
                        map[i][j + 1] = ''
                elif map[i][j] == 'H' and map[i - 1][j] != 'H':
                    map[i - 1][j] = ''
                    # clear right left end of ladder
                    if j-1 >= 0:
                        map[i][j-1] = '#'
                        map[i-1][j - 1] = ''
                    if j + 1 <= 27:
                        map[i][j + 1] = '#'
                        map[i - 1][j + 1] = ''
            if i != 15:
                if map[i][j] == 'H' and map[i + 1][j] != 'H':
                    if j-1 >= 0:
                        map[i+1][j-1] = '#'
                    if j + 1 <= 27:
                        map[i+1][j + 1] = '#'
                    map[i + 1][j] = '#'


def fill_too_small_gaps(map):
    for i in range(0, 16):
        for j in range(0, 28):
            if map[i][j] == '' or map[i][j] == '$' or map[i][j] == '0' or map[i][j] == '&':
                if j - 1 >= 0 and j + 1 <= 27:
                    if (map[i][j+1] == '#' or map[i][j+1] == '@' or map[i][j+1] == 'X') and (map[i][j-1] == '#' or map[i][j-1] == '@' or map[i][j-1] == 'X'):
                        if i != 15 and (map[i+1][j] == '#' or map[i+1][j] == '@' or map[i+1][j] == 'X'):
                            map[i][j] = '#'
                elif j + 1 <= 27 and (map[i][j + 1] == '#' or map[i][j + 1] == '@' or map[i][j + 1] == 'X'):
                    if i != 15 and (map[i+1][j] == '#' or map[i+1][j] == '@' or map[i+1][j] == 'X'):
                        map[i][j] = '#'
                elif j - 1 >= 0 and (map[i][j - 1] == '#' or map[i][j - 1] == '@' or map[i][j - 1] == 'X'):
                    if i != 15 and (map[i+1][j] == '#' or map[i+1][j] == '@' or map[i+1][j] == 'X'):
                        map[i][j] = '#'


def mock_map():
    level = "                  S         " +\
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