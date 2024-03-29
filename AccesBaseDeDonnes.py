from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from dependency import pickle

"""Sauvegarder la variable load_data avec pickle"""
# the data, shuffled and split between train and test sets
#plt.figure(figsize=(7.195, 3.841), dpi=100)
#for i in range(10):
  #plt.subplot(10,20,i+1)
 # plt.imshow(X_train[i,:].reshape([28,28]), cmap='gray')
 # plt.axis('off')
#plt.show()

def Get_image_And_Label(i):
  X_train, label = Load_Data_From_Pickle()
  #print("label : ", label[i])
  #plt.figure()
  #plt.imshow(X_train[i,:].reshape([28,28]), cmap='gray')
  #plt.show()
  return X_train[i], label[i]


def Get_proportion0():
  X0 = Load_Data()
  return np.mean(X0)

def Load_Data():
  (X_train, y_train), (X_test, y_test) = mnist.load_data()
  y_train = y_train.reshape(60000,)
  X_train = X_train.reshape(60000, 784)
  X_test = X_test.reshape(10000, 784)
  X_train = X_train.astype('float32')
  X_test = X_test.astype('float32')
  X_train /= 255
  X_test /= 255
  return X_train, y_train

def Save_Data_Base():
  X_train, y_train = Load_Data()
  try:
    with open("mnist_data_base.pickle", "wb") as f:
      pickle.dump((X_train, y_train), f, protocol=pickle.HIGHEST_PROTOCOL)#Warning with highest protocol peut être incompatible avec certaines version de python
  except Exception as ex:
    print("Error during pickling object (Possibly unsupported):", ex)

 
def Load_Data_From_Pickle() :
  try:
    with open("mnist_data_base.pickle", "rb") as f:
      return pickle.load(f)
  except Exception as ex:
    print("Error during unpickling object (Possibly unsupported):", ex)

#print(Get_proportion0())
#Get_image_And_Label(0)
#Save_Data_Base()
#Get_image_And_Label(5)



