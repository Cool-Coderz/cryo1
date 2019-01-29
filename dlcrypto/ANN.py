# Neural Network
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv1D, MaxPooling1D, LeakyReLU, PReLU
from keras.utils import np_utils
from keras.callbacks import CSVLogger, ModelCheckpoint
from sklearn.preprocessing import MinMaxScaler
import pickle
import pandas as pd

df = pd.read_pickle(path='./cryptocompare_daily_BTCUSD.pkl')
df
# Clean up the data real quick
df.fillna(0, inplace=True)

columns = df.columns
scaler = MinMaxScaler()
# normalization
for c in columns[4:8]:
    df[c] = scaler.fit_transform(df[c].values.reshape(-1,1))
df
