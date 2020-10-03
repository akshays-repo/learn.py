from keras import utils as np_utils
from keras.layers import Dense
from keras.models import Sequential
import numpy as np
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5


# flatten
train_images = train_images.reshape((-1, 784))
test_images = test_images.reshape((-1, 784))
print(train_images.shape)
print(test_images.shape)


model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax'),
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

model.fit(
    train_images,
    np_utils.to_categorical(train_labels),
    epochs=5,
    batch_size=32,
)
model.evaluate(
    test_images,
    np_utils.to_categorical(test_labels)
)
