from music21 import stream, note, chord
import random


# --------------------------------------------------
# Load vocabulary
# --------------------------------------------------

with open("midi_data/notes.txt", "r") as file:
    notes = [
        line.strip()
        for line in file
        if line.strip()
    ]


# Remove duplicates while preserving order
vocabulary = list(dict.fromkeys(notes))

print("Vocabulary size:", len(vocabulary))


# --------------------------------------------------
# Generate musical sequence
# --------------------------------------------------

generated_sequence = []

sequence_length = 100

for _ in range(sequence_length):
    generated_sequence.append(
        random.choice(vocabulary)
    )


print("Generated elements:", len(generated_sequence))


# --------------------------------------------------
# Convert generated sequence to music21
# --------------------------------------------------

music = stream.Stream()

for item in generated_sequence:

    # Chord
    if "." in item:

        pitch_classes = [
            int(value)
            for value in item.split(".")
        ]

        new_chord = chord.Chord(
            pitch_classes
        )

        new_chord.quarterLength = 0.5

        music.append(new_chord)

    # Single note
    else:

        new_note = note.Note(item)

        new_note.quarterLength = 0.5

        music.append(new_note)


# --------------------------------------------------
# Save generated MIDI
# --------------------------------------------------

output_file = "generated_music.mid"

music.write(
    "midi",
    fp=output_file
)


print("MUSIC GENERATED SUCCESSFULLY")
print("Output file:", output_file)
