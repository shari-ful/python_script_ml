import mnist
import pickle
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers, models


x_train, x_test, y_train, y_test = mnist.train_images(), mnist.test_images(), mnist.train_labels(), mnist.test_labels()
x_train, x_test = x_train / 255, x_test / 255

y_train, y_test = to_categorical(y_train), to_categorical(y_test)

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.2)

test_loss, test_accuracy = model.evaluate(x_test, y_test)

print(test_accuracy)
