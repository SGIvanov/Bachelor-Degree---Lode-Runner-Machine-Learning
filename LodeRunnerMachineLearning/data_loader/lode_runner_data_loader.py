import os
from data_loader.base_data_loader import BaseDataLoader


class LodeRunnerDataLoader(BaseDataLoader):
    def __init__(self, config):
        super(LodeRunnerDataLoader, self).__init__(config)
        self.token_list = self.read_tokens()
        (self.X_train_matrix, self.X_test_matrix) = self.load_training_data_matrix()
        print('Transform loaded levels into neuronal network inputs')
        (self.X_train, self.y_train) = self.create_vectorized_data(self.X_train_matrix)
        (self.X_test, self.y_test) = self.create_vectorized_data(self.X_test_matrix)

    def get_train_data_matrix(self):
        return self.X_train_matrix

    def get_test_data_matrix(self):
        return self.X_test_matrix

    def get_train_data(self):
        return self.X_train, self.y_train

    def get_test_data(self):
        return self.X_test, self.y_test

    def read_tokens(self):
        print('Loading Dictionary of Tokens into memory...', end='    ')
        tokens = []
        dir_name = os.path.dirname(__file__)
        filename = os.path.join(dir_name, '../utils/Others/'+self.config.token_dictionary_name)
        with open(filename, 'r') as fin:
            for line in fin:
                tokens.append(line[0])
        print('Done')
        print('Tokens: ' + str(tokens))
        return tokens

    def load_training_data_matrix(self):
        print('Loading ' + str(self.config.number_of_levels_to_load)+ ' levels')
        print('  Loading ' + str(self.config.number_of_levels_to_train_on) + ' training levels into memory')
        if self.config.number_of_levels_to_train_on + self.config.number_of_levels_to_test_on \
                != self.config.number_of_levels_to_load:
            raise ValueError("Inconsistent size of train/test data set")
        train_matrix, test_matrix = [], []
        dir_root = os.path.dirname(__file__)
        dir_name = os.path.join(dir_root, '../utils/Others/Levels_DataSet/')
        w, h = self.config.level_number_of_columns, self.config.level_number_of_lines
        for i in range(1, self.config.number_of_levels_to_train_on+1):
            level_name = self.config.level_name_prefix+str(i)+self.config.level_file_extension
            level_file = os.path.join(dir_name, level_name)
            matrix = [[' ' for _ in range(w)] for _ in range(h)]
            with open(level_file,'r') as fin:
                for line_no, line in enumerate(fin, 0):
                    for j in range(0, self.config.level_number_of_columns):
                        matrix[line_no][j] = line[j]
            train_matrix.append(matrix)
            print('   --LevelTrain: ' + str(i) + ' loaded successfully')
        print('  Training levels loaded successfully')
        print()
        print('  Loading ' + str(self.config.number_of_levels_to_test_on) + ' testing levels into memory')
        for i in range(self.config.number_of_levels_to_train_on+1, self.config.number_of_levels_to_load+1):
            level_name = self.config.level_name_prefix+str(i)+self.config.level_file_extension
            level_file = os.path.join(dir_name, level_name)
            matrix = [[' ' for _ in range(w)] for _ in range(h)]
            with open(level_file,'r') as fin:
                for line_no, line in enumerate(fin, 0):
                    for j in range(0, self.config.level_number_of_columns):
                        matrix[line_no][j] = line[j]
            test_matrix.append(matrix)
            print('   --LevelTest: ' + str(i) + ' loaded successfully')
        print('  Testing levels loaded successfully')
        print()
        print('All levels loaded successfully')
        print()
        return train_matrix, test_matrix

    def create_vectorized_data(self, list_of_data_matrix):
        # parse each matrix in the list
        x_test, y_test = [], []
        for i in range(0, len(list_of_data_matrix)):
            print('Transforming level: ' + str(i + 1) + ' out of ' + str(len(list_of_data_matrix)) + ' ...', end='   ')
            # parse the level matrix (On Columns sneak stile)
            k = 0
            sign = True
            for j in range(0, self.config.level_number_of_columns):
                if k == 16:
                    k = 15
                    sign = False
                elif k == -1:
                    k = 0
                    sign = True
                while 16 > k > -1:
                    token = (list_of_data_matrix[i])[k][j]
                    if token == '#':
                        vector = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    elif token == '@':
                        vector = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
                    elif token == 'H':
                        vector = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
                    elif token == '-':
                        vector = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
                    elif token == 'X':
                        vector = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
                    elif token == 'S':
                        vector = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
                    elif token == '$':
                        vector = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
                    elif token == '0':
                        vector = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
                    elif token == '&':
                        vector = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
                    else:
                        vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                    if j != 0 or k != 0:
                        y_test.append(vector)
                    if k != self.config.level_number_of_lines-1 or j != self.config.level_number_of_columns-1:
                        x_test.append(vector)
                    if sign:
                        k += 1
                    else:
                        k -= 1
            print('Done')
        print()
        return x_test, y_test
