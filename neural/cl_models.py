'''
Created on 01.04.2019

@author: pawel
'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def perceptron():
    model = Sequential()
    model.add(Dense(1, activation='sigmoid'))
    return model

def hidden_linear():
    model = Sequential()
    model.add(Dense(50, input_dim=2))
    model.add(Dense(1, activation='sigmoid'))
    return model

def hidden_sigmoid():
    model = Sequential()
    model.add(Dense(50, input_dim=2, activation='sigmoid'))
    model.add(Dense(1, activation='sigmoid'))
    return model

def hidden_relu():
    print('akuku')
    model = Sequential()
    model.add(Dense(50, input_dim=2, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model
