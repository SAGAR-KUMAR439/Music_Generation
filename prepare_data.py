from music21 import converter, note, chord


midi_file = "midi_data/wiegenlied.mid"

score = converter.parse(midi_file)

notes = []


for element in score.flatten().notes:

    if isinstance(element, note.Note):
        notes.append(str(element.pitch))

    elif isinstance(element, chord.Chord):
        notes.append(
            ".".join(str(n) for n in element.normalOrder)
        )


print("Total musical elements:", len(notes))


# Create vocabulary
vocab = sorted(set(notes))

note_to_int = {
    item: number
    for number, item in enumerate(vocab)
}


# Convert musical elements to numbers
encoded_notes = [
    note_to_int[item]
    for item in notes
]


print("Unique elements:", len(vocab))
print("Encoded elements:", len(encoded_notes))


# Create training sequences
sequence_length = 20

input_sequences = []
output_values = []


for i in range(
    len(encoded_notes) - sequence_length
):

    sequence = encoded_notes[
        i:i + sequence_length
    ]

    target = encoded_notes[
        i + sequence_length
    ]

    input_sequences.append(sequence)
    output_values.append(target)


print("Training sequences:", len(input_sequences))
print("Sequence length:", sequence_length)


# Save encoded dataset
with open(
    "midi_data/encoded_notes.txt",
    "w"
) as file:

    for sequence, target in zip(
        input_sequences,
        output_values
    ):

        file.write(
            ",".join(map(str, sequence))
            + "|"
            + str(target)
            + "\n"
        )


print("ENCODED DATASET SAVED SUCCESSFULLY")
