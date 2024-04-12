import os
import librosa
import soundfile as sf
import shutil

def move_audio_files(directory, mono_directory, stereo_directory):

    os.makedirs(mono_directory, exist_ok=True)
    os.makedirs(stereo_directory, exist_ok=True)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path} ...")
                audio, sr = librosa.load(file_path, sr=None, mono=False)
                if audio.ndim != 2 or audio.shape[0] < 2:
                    print(f"File {file_path} is not stereo. Moving to mono directory.")
                    shutil.move(file_path, os.path.join(mono_directory, file))
                else:
                    shutil.move(file_path, os.path.join(stereo_directory, file))

# Usage
move_audio_files("D:/datasets/reverbs/data", "D:/datasets/reverbs/data/reverb-mono", "D:/datasets/reverbs/data/reverb-stereo")