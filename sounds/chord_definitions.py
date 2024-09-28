# Chord definitions corresponding to each note with mapping numbers
chord_definitions = {
    'C4': (['C4', 'E4', 'G4'], 1),    # C Major
    'D4': (['D4', 'F#4', 'A4'], 2),   # D Major
    'E4': (['E4', 'G#4', 'B4'], 3),   # E Major
    'F4': (['F4', 'A4', 'C5'], 4),    # F Major
    'G4': (['G4', 'B4', 'D5'], 5),    # G Major
    'A4': (['A4', 'C#5', 'E5'], 6),   # A Major
    'Bb4': (['Bb4', 'D5', 'F5'], 7),  # Bb Major
}

# Frequencies for musical notes
frequencies = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'Bb4': 466.16,
    'C5': 523.25,
}

# # Function to analyze melody and generate chords
# def generate_chords_from_melody(melody):
#     chords = []
#     mapping_values = []  # List to hold mapping values
#
#     for note in melody:
#         if note in chord_definitions:  # Check if the note has a chord definition
#             chord, mapping_number = chord_definitions[note]  # Get the chord and its mapping number
#             chords.append(f"Chord based on {note} - Mapped Number: {mapping_number}")
#             mapping_values.append(mapping_number)  # Store the mapping number
#
#     return chords, mapping_values
