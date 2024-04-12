import os
import librosa
import soundfile as sf

def trim_audio_files(directory, output_directory, duration=5):
    os.makedirs(output_directory, exist_ok=True)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                print(f"Trimming {file_path} ...")
                audio, sr = librosa.load(file_path, sr=None, mono=True)
                audio = librosa.util.fix_length(audio, size=sr * duration)
                output_file = os.path.join(output_directory, file)
                sf.write(output_file, audio.T, sr, format='WAV', subtype='PCM_16')
                print(f"Saved {output_file}")

# Usage
trim_audio_files("D:/datasets/reverbs/data/reverb-mono", "D:/datasets/reverbs/data/reverb-mono-5", duration=5)