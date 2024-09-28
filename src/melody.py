import librosa
import numpy as np

class Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration

# def analyze_melody(file_path):
#     # Load audio file
#     try:
#         y, sr = librosa.load(file_path)
#     except Exception as e:
#         print(f"Error loading file: {e}")
#         return []
#
#     # Extract pitches and magnitudes
#     pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
#     melody = []
#
#     # Filter and process pitches
#     for i in range(pitches.shape[1]):
#         index = magnitudes[:, i].argmax()
#         pitch = pitches[index, i]
#         if pitch > 0:  # Only consider positive pitches
#             try:
#                 note = librosa.hz_to_note(pitch)
#                 melody.append(Note(pitch=note, duration=1.0))  # Fixed duration for now
#             except Exception as e:
#                 print(f"Error converting frequency {pitch}: {e}")
#
#     return melody

def analyze_melody(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

        melody = []
        for i in range(pitches.shape[1]):
            index = magnitudes[:, i].argmax()
            pitch = pitches[index, i]
            if pitch > 0:
                note = librosa.hz_to_note(pitch)
                melody.append(note)

        # If no notes are extracted, print a message
        if not melody:
            print("No melody extracted.")
        return melody
    except Exception as e:
        print(f"Error analyzing melody: {e}")
        return []


# def generate_chords_from_melody(melody):
#     # Generate chords from the melody
#     chords = []
#     for note in melody:
#         chord = f"Chord based on {note.pitch}"  # Simple chord generation for demonstration
#         chords.append(chord)
#     return chords

def generate_chords_from_melody(melody):
    chords = []
    for note in melody:
        if note:
            # Generate a simple chord based on the note (just an example)
            base_note = note[0]  # Use the first character as the base note
            chord = f"{base_note} major"  # Simple chord type for demonstration
            chords.append(f"Chord based on {note}: {chord}")
    print(f"Generated chords: {chords}")  # Debugging statement
    return chords


def main(file_path):
    melody = analyze_melody(file_path)
    if not melody:
        print("No melody extracted.")
        return

    chords = generate_chords_from_melody(melody)
    for chord in chords:
        print(chord)

if __name__ == "__main__":
    file_path = "C:\\Users\\nabha\\Desktop\\final_project\\Chords\\pythonProject1\\audio\\Ed Sheeran - Shivers (Lyrics).mp3"  # Replace with your actual audio file
    main(file_path)
