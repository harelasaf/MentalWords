import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, GlobalAveragePooling1D, MaxPooling1D, Conv1D
from sklearn.model_selection import train_test_split

# Load previous files
imageDirectory = np.load('imageDirectory.npy')
answerDirectory = np.load('answerDirectory.npy')
imageLength = 110 # arbitrary, but needs to be exactly like reConstructData.py

# Turn answerDirectory into one-hot array
oneHotAnswers = np.zeros((answerDirectory.size,3)) #initialize one-hot array
answerDirectory = answerDirectory.astype(np.int64) # turn into int (from float)
answerDirectory = np.subtract(answerDirectory,1) # subtract 1 from each answer so it will start from 0
oneHotAnswers[np.arange(answerDirectory.size),(answerDirectory)] = 1 # set the one-hot array


# Split to Training and Testing Set
X_train, X_test, y_train, y_test = train_test_split(imageDirectory, oneHotAnswers, test_size=0.3)

# Build Model
model = Sequential()
model.add(Conv1D(40, 10, strides=2, padding='same', activation='relu', input_shape=(imageLength, 4)))
model.add(Dropout(0.2))
model.add(MaxPooling1D(3))
model.add(GlobalAveragePooling1D())
model.add(Dense(50, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Train Model
model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=100, epochs=300)

# Test Model
y_predicted = model.predict(X_test)
print(y_predicted)