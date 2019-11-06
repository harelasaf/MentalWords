# Separate words
import numpy as np
import pandas as pd

path = 'C:\BGU Google Drive\projects\MentalWords\MentalWords\data_2019-11-03-09.53.14.csv'
my_data1 = pd.read_csv(path, sep=',', header=0)
del my_data1['timestamps']
del my_data1['Marker']
A = my_data1.ix[:, 2]
B = my_data1.ix[:, 3]
C = my_data1.ix[:, 4]
D = my_data1.ix[:, 5]
terms = my_data1.ix[:, 1]
words = my_data1.ix[:, 0]
class_names = ['MEXICANI','KAPIOT','KARNAF']
classes = my_data1.ix[:,6]
my_data = np.zeros((5, 39600))
my_data[0] = (words)
my_data[1] = (A)
my_data[2] = (B)
my_data[3] = (C)
my_data[4] = (D)
my_data = np.transpose(my_data)


lineIndex = 0
currentWord = 2
imageLength = 110
currentImage = np.zeros(4)
imageDimensions = (imageLength, 4)
imageDirectory = np.zeros(imageDimensions)
answerDirectory = np.zeros(1)

while lineIndex < terms.shape[0]:
    currentLine = np.array(my_data[lineIndex])
    if int(currentLine[0]) == currentWord:
        currentImage = np.vstack((currentImage, currentLine[1:]))
    else:
        currentImageTrimmed = np.delete(currentImage, 0, 0)
        currentImageTrimmed = np.vsplit(currentImageTrimmed, ([imageLength]))[0]
        if currentImageTrimmed.shape[0] < imageLength:
            print("ERROR: Invalid Image at currentWord = " + str(currentWord))
            exit(1)
        imageDirectory = np.dstack((imageDirectory, currentImageTrimmed))
        answerDirectory = np.vstack((answerDirectory, classes[lineIndex]))
        print(str(imageDirectory.shape) + "\n")
        currentImage = np.zeros(4)
        currentWord = currentLine[0]
    lineIndex += 1

imageDirectory = np.transpose(imageDirectory, (2, 0, 1))
imageDirectory = np.delete(imageDirectory, 0, 0)
answerDirectory = np.delete(answerDirectory, 0, 0)
np.save('imageDirectory.npy', imageDirectory)
answerDirectory = [answerDirectory - 1 for answerDirectory]
np.save('answerDirectory.npy', answerDirectory)