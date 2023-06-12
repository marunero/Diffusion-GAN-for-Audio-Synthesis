import librosa
import numpy as np
from PIL import Image

import argparse

#########################################################################
#######################  Audio -> melspectrogram  #######################  

def wav2spec(filename):
  audio, sr = librosa.load(filename)
  audio = np.clip(audio, 1e-5, 1e5)

  # converting audio np array to spectrogram
  spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_fft=1024, hop_length=256, win_length=1024, window='hann', center=True, pad_mode='reflect', power=2.0, n_mels=87)

  return spectrogram

def main(args):
    spec = wav2spec(args['input'])

    # log scaling & convert to uint8
    spec = np.log10(spec)
    spec = np.clip(spec, -5, 5)
    spec = (spec / 10 + 0.5) * 255
    spec = spec.astype(np.uint8)
    spec = np.tile(spec[:, :, np.newaxis], (1, 1, 3))

    img = Image.fromarray(spec)
    
    img.save(args['save'])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--save", help="output melspectrogram path", default="output.png")
    parser.add_argument("-i", "--input", help="input audio path", default="input.wav")

    args = vars(parser.parse_args())

    main(args)