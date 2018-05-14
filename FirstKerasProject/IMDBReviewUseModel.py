import numpy as np
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM , CuDNNLSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.models import load_model

np.random.seed(7)
# load the dataset but only keep the top n words, zero the rest
top_words = 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
# truncate and pad input sequences
max_review_length = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)

model = load_model('10E_64B_Acc86.47%_240s_CudnnLSTM_model-16sEval.h5')
print(y_test[1])
print(y_test[50])
print(y_test[100])
print(model.predict(np.array([X_test[1],X_test[50],X_test[100]]),verbose=1))
