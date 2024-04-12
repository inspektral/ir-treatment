import os
import librosa
import soundfile as sf

def split_audio_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                print(f"Splitting {file_path} ...")
                audio, sr = librosa.load(file_path, sr=None, mono=False)
                if audio.ndim != 2 or audio.shape[0] < 2:
                    print(f"File {file_path} is not stereo. Skipping.")
                    continue
                sf.write(file_path.replace('.wav', '-left.wav'), audio[0], sr)
                sf.write(file_path.replace('.wav', '-right.wav'), audio[1], sr)

# Usage
split_audio_files("D:/datasets/reverbs/data")