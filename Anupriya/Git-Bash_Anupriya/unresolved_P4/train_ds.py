#!/usr/bin/env python
import sys

batch=sys.argv[1]
epoch_num=sys.argv[2]
class_num=sys.argv[3]

print("Batch: ",batch, "Epochs: ",epoch_num,"Classes : ",class_num)

import numpy as np
import os
import PIL
# import PIL.Image32 10
import tensorflow as tf
from tensorflow.keras import layers

#setting important parameters and loading the three required datasets
img_height = 180
img_width = 180
data_dir= "dataset"
#using bigger dataset for now
data_dir_new="dataset"
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir_new,
  label_mode='int', 
  validation_split=0.1,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch)

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir_new,
  validation_split=0.1,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch)
class_names = train_ds.class_names
print(class_names)

#creating test_ds and loading images
img_height = 180
img_width = 180
test_dir= "dataset"
test_ds = tf.keras.utils.image_dataset_from_directory(
  test_dir,  
  image_size=(img_height, img_width),
  batch_size=batch)

test_ds = test_ds.map(lambda x, y: (tf.keras.applications.resnet50.preprocess_input(x), y))

for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break

#autotuning data and applying prefetch
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

# creating data augmentation layer
data_augmentation = tf.keras.Sequential([
  tf.keras.layers.RandomFlip('horizontal'),
  tf.keras.layers.RandomRotation(0.1),
  tf.keras.layers.RandomContrast(factor=0.3),

])

# creating normalisation layer to rescale image
normalization_layer = tf.keras.layers.Rescaling(1./255)

# printing min and max pixel value of image after normalization
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixel values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))

#initial sequential network built

num_classes = class_num

model41 = tf.keras.Sequential([
  normalization_layer,
  data_augmentation,
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes)
])

# compiling sequential model
model41.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

#finding the right value of epochs is tough as we might risk overfitting the model i.e., when accuracy > val_accuracy
model41.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epoch_num
)

#saving model so that we don't have to do the above steps again
model41.save('model')