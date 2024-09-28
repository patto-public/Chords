from flask import Flask, render_template, request
import librosa
import numpy as np
import os

app = Flask(__name__)

# Note to frequency mapping (expanded)
note_mapping = {
    'C4': 261.63,
    'C#4': 277.18,
    'D4': 293.66,
    'D#4': 311.13,
    'E4': 329.63,
    'F4': 349.23,
    'F#4': 369.99,
    'G4': 392.00,
    'G#4': 415.30,
    'A4': 440.00,
    'A#4': 466.16,
    'B4': 493.88,
    'C5': 523.25,
    'C#5': 554.37,
    'D5': 587.33,
    'D#5': 622.25,
    'E5': 659.25,
    'F5': 698.46,
    'F#5': 739.99,
    'G5': 783.99,
    'G#5': 830.61,
    'A5': 880.00,
    'A#5': 932.33,
    'B5': 987.77,
}


def analyze_audio(file_path):
    """
    Analyze the audio file to extract frequencies.
    """
    y, sr = librosa.load(file_path)
    # Get the frequencies and magnitudes
    frequencies = np.abs(librosa.stft(y))
    magnitudes = np.abs(frequencies).sum(axis=0)

    # Get the indices of the peaks in the magnitude spectrum
    peak_indices = np.argwhere(magnitudes > np.mean(magnitudes)).flatten()

    # Limit the indices to the size of the frequency array
    peak_indices = peak_indices[peak_indices < frequencies.shape[0]]

    # Ensure we return frequencies without exceeding bounds
    return librosa.core.fft_frequencies(sr=sr)[peak_indices]


def analyze_frequencies(frequencies):
    """
    Analyzes the list of frequencies and returns their corresponding chords.
    :param frequencies: List of frequency values (float) to analyze
    :return: List of chords with frequencies and their mapped numbers
    """
    frequency_to_note = {v: k for k, v in note_mapping.items()}
    chords = []
    threshold = 5.0  # Allowable deviation in Hz for matching

    for frequency in frequencies:
        closest_note = None
        mapped_number = None
        for note_freq, note in frequency_to_note.items():
            if abs(note_freq - frequency) <= threshold:
                closest_note = note
                mapped_number = list(frequency_to_note.keys()).index(note_freq) + 1  # Start numbering from 1
                break

        if closest_note:
            chords.append(
                f"Chord based on {closest_note} - Frequency: {frequency:.2f} - Mapped Number: {mapped_number}")
        else:
            chords.append(f"Frequency: {frequency:.2f} - Note: Not Mapped")

    return chords


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        file = request.files['file']
        uploads_dir = './uploads'
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        file_path = os.path.join(uploads_dir, file.filename)
        file.save(file_path)

        # Analyze audio and frequencies
        frequencies = analyze_audio(file_path)
        chords = analyze_frequencies(frequencies)  # Corrected spelling

        return render_template('result.html', chords=chords)


if __name__ == '__main__':
    app.run(debug=True)
