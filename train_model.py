import os

# TensorFlow ko load karne se PEHLE ye settings honi chahiye
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense


# --------------------------------------------------
# TensorFlow CPU settings
# --------------------------------------------------

tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)


# --------------------------------------------------
# Load encoded dataset
# --------------------------------------------------

data = []

with open("midi_data/encoded_notes.txt", "r") as file:

    for line in file:

        line = line.strip()

        if not line:
            continue

        sequence, target = line.split("|")

        sequence = [
            int(value)
            for value in sequence.split(",")
        ]

        target = int(target)

        data.append((sequence, target))


# --------------------------------------------------
# Convert dataset to NumPy arrays
# --------------------------------------------------

X = np.array(
    [item[0] for item in data],
    dtype=np.int32
)

y = np.array(
    [item[1] for item in data],
    dtype=np.int32
)


print("Input shape:", X.shape, flush=True)
print("Target shape:", y.shape, flush=True)


# --------------------------------------------------
# Dataset information
# --------------------------------------------------

vocab_size = 26
sequence_length = X.shape[1]


print("Vocabulary size:", vocab_size, flush=True)
print("Sequence length:", sequence_length, flush=True)


# --------------------------------------------------
# Build LSTM model
# --------------------------------------------------

model = Sequential([

    Input(shape=(sequence_length,)),

    Embedding(
        input_dim=vocab_size,
        output_dim=32
    ),

    LSTM(64),

    Dense(
        vocab_size,
        activation="softmax"
    )
])


# --------------------------------------------------
# Compile model
# --------------------------------------------------

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)


print("\nMODEL ARCHITECTURE:", flush=True)

model.summary()


# --------------------------------------------------
# Training
# --------------------------------------------------

print("\nSTARTING TRAINING...", flush=True)


history = model.fit(
    X,
    y,
    epochs=30,
    batch_size=8,
    verbose=1,
    shuffle=True
)


# --------------------------------------------------
# Save trained model
# --------------------------------------------------

print("\nSaving trained model...", flush=True)

model.save("music_model.keras")


print("\nMODEL TRAINED AND SAVED SUCCESSFULLY", flush=True)
print("Model file: music_model.keras", flush=True)
