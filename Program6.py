import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pickle


mnist = tf.keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

X_train = tf.keras.utils.normalize(X_train)
X_test = tf.keras.utils.normalize(X_test)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape = (28,28)))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=3)
loss, accuracy = model.evaluate(X_test, Y_test)
print('Loss: ', loss)
print('Accuracy: ', accuracy)

with open('model.pickle', 'wb') as file:
    pickle.dump(model, file)


import  cv2 as cv
imagine_path = "c:/Users/pawko/OneDrive/Pulpit/python/machine_learning/jeden.png"
image = cv.imread(imagine_path)[:,:,0]
image = np.invert(np.array([image]))

#single_image = np.expand_dims(image, axis=0)
prediction = model.predict(image)
print("Prediction: {}".format(np.argmax(prediction)))
plt.imshow(image[0])
plt.show()
#Program został napisany przy pomocy książki python Bible autorstwa Floriana Dedova