from keras.datasets import mnist
import matplotlib.pyplot as plt
# the data, shuffled and split between train and test sets
#plt.figure(figsize=(7.195, 3.841), dpi=100)
#for i in range(10):
  #plt.subplot(10,20,i+1)
 # plt.imshow(X_train[i,:].reshape([28,28]), cmap='gray')
 # plt.axis('off')
#plt.show()

def Get_image():
  (X_train, y_train), (X_test, y_test) = mnist.load_data()
  X_train = X_train.reshape(60000, 784)
  X_test = X_test.reshape(10000, 784)
  X_train = X_train.astype('float32')
  X_test = X_test.astype('float32')
  X_train /= 255
  X_test /= 255
  return X_train[0]