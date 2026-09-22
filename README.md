# Music Generation

A Python-based music generation project developed as part of the **Artificial Intelligence Internship**.

This project demonstrates MIDI music processing using **music21**, numerical data preprocessing using **NumPy**, and a prototype approach for generating new MIDI sequences.

---

## 🎵 Project Overview

The objective of this project is to explore the process of:

* Collecting MIDI music data
* Processing MIDI files using `music21`
* Extracting notes and chords
* Converting musical elements into numerical representations
* Creating sequential training data
* Generating a new MIDI file
* Loading and verifying the generated MIDI output

The project was developed as part of **Task 3 — Music Generation** of the AI Internship.

---

## 🛠️ Technologies Used

* **Python 3.10**
* **music21**
* **NumPy**
* **MIDI**
* **TensorFlow / Keras** — explored for LSTM-based training

---

## 📂 Project Structure

```text
CodeAlpha_Music_Generation/
│
├── midi_data/
│   ├── lc5701612.mscx
│   ├── wiegenlied.mid
│   ├── encoded_notes.txt
│   └── notes.txt
│
├── prepare_data.py
├── train_model.py
├── generate_music.py
├── generated_music.mid
└── README.md
```

---

## 🎼 Dataset

The source musical score was obtained from the **OpenScore Lieder** collection.

The selected piece is:

**Johannes Brahms — Wiegenlied**

The original MuseScore file was converted into MIDI format and processed using `music21`.

---

## 🔄 Data Preprocessing

The MIDI file was loaded using `music21`.

The musical elements were extracted as:

* Individual notes
* Chords

Each musical element was converted into a string representation.

For example:

```text
C5
D5
E-5
3.7.10
5.8
```

The extracted dataset contained:

```text
Total musical elements: 365
Unique elements: 26
```

The musical elements were then converted into integer IDs.

A sequence length of **20** was used to create sequential input data.

The resulting dataset contained:

```text
Training sequences: 345
Sequence length: 20
```

The processed dataset was saved as:

```text
midi_data/encoded_notes.txt
```

---

## 🧠 LSTM Model Exploration

An LSTM-based neural network was implemented using TensorFlow/Keras to explore the deep-learning approach described in the internship task.

The model architecture included:

* Embedding layer
* LSTM layer
* Dense output layer
* Softmax activation

The intended architecture was designed to predict the next musical element from a sequence of previous musical elements.

However, during execution, TensorFlow's native numerical operations terminated unexpectedly on the available legacy CPU environment.

Because the training process could not be completed reliably on the available hardware, the project does **not** claim that a trained LSTM model successfully generated the final MIDI file.

---

## 🎵 MIDI Generation Prototype

To demonstrate the complete MIDI generation pipeline, a prototype generator was implemented.

The generator:

1. Loads the extracted musical vocabulary.
2. Selects musical elements from the vocabulary.
3. Creates a sequence of 100 elements.
4. Converts notes and chords into `music21` objects.
5. Creates a MIDI stream.
6. Saves the generated music as:

```text
generated_music.mid
```

The generated MIDI file was successfully verified using `music21`.

Verification result:

```text
GENERATED MIDI LOADED SUCCESSFULLY
Parts: 1
Elements: 100
```

> **Important:** The current `generated_music.mid` is a functional prototype generated from the musical vocabulary. It is not the output of a successfully trained LSTM model.

---

## ▶️ How to Run

### 1. Install dependencies

Open Command Prompt in the project folder and run:

```bash
py -m pip install music21 numpy
```

If TensorFlow experimentation is required:

```bash
py -m pip install tensorflow
```

---

### 2. Prepare the dataset

Run:

```bash
py prepare_data.py
```

This extracts musical elements and creates sequential encoded data.

---

### 3. Generate MIDI

Run:

```bash
py generate_music.py
```

The generated MIDI file will be created as:

```text
generated_music.mid
```

---

### 4. Verify the generated MIDI

Run:

```bash
py -c "from music21 import converter; score=converter.parse('generated_music.mid'); print('GENERATED MIDI LOADED SUCCESSFULLY'); print('Parts:', len(score.parts)); print('Elements:', len(score.flatten().notes))"
```

---

## 📊 Results

The project successfully demonstrated:

| Component                           | Status           |
| ----------------------------------- | ---------------- |
| MIDI dataset collection             | ✅                |
| MIDI parsing                        | ✅                |
| Note/chord extraction               | ✅                |
| Data encoding                       | ✅                |
| Sequential dataset creation         | ✅                |
| MIDI generation                     | ✅                |
| Generated MIDI validation           | ✅                |
| LSTM model implementation           | ✅                |
| LSTM training on available hardware | ⚠️ Not completed |
| Trained AI music generation         | ⚠️ Not completed |

---

## 📌 Learning Outcomes

Through this project, the following concepts were explored:

* MIDI music representation
* Music21 library
* Musical notes and chords
* Data preprocessing
* Vocabulary creation
* Integer encoding
* Sequential data preparation
* LSTM-based music generation concepts
* MIDI file generation
* AI/ML development constraints on legacy hardware

---

## 🚀 Future Improvements

The project can be extended by running the LSTM training on a compatible modern CPU/GPU or cloud environment.

Possible improvements include:

* Training a complete LSTM model
* Using a larger MIDI dataset
* Generating longer musical sequences
* Improving chord and rhythm handling
* Adding temperature-based sampling
* Creating a web interface for music generation
* Converting generated MIDI into audio
* Experimenting with RNN, LSTM, or GAN architectures

---

## 📜 Internship

This project was developed for:

**Artificial Intelligence Internship**

Task:

**Task 3 — Music Generation**

---

## 👨‍💻 Author

**SAGAR**

GitHub:

https://github.com/SAGAR-KUMAR439

---

## 📄 License

This project is created for educational and internship purposes.
