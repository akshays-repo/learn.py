import numpy as np
import mnist

train_images = mnist.train.images()
train_labels = mnist.train.labels()
test_images = mnist.test.images()
test_labels = mnist.test.labels()

#normlise

train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5


#flatten
train_images =train_images.reshape((-1 ,784))
test_images =test_images.reshape((-1 ,784))

print(train_images.shape)
print(test_images.shape)

form keras.models import Sequential
from keras.layers import Dense

#Build model

model = Sequential([
    Dense(64, activation='relu', input_shape=(784)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax'),

])

#compile

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

#Train
model.fit(train_images,
    to_categorical(train_label), batch_size=32, epochs=5)

model.evaluate(
    test_images,
    to_categorical(test_labels)
)
