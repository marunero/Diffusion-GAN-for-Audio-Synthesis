import librosa
import numpy as np
from diffwave.params import params
from PIL import Image

#########################################################################
#######################  Audio -> melspectrogram  #######################  

def wav2spec(filename):
  audio, sr = librosa.load(filename)
  audio = np.clip(audio, 1e-5, 1e5)

  # converting audio np array to spectrogram
  spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_fft=params.n_fft, hop_length=params.hop_samples, win_length=params.hop_samples * 4, window='hann', center=True, pad_mode='reflect', power=2.0, n_mels=87)

  return spectrogram


def mel(filename_wav):
    spec = wav2spec(filename_wav)

    # log scaling & convert to uint8
    spec = np.log10(spec)
    spec = np.clip(spec, -5, 5)
    spec = (spec / 10 + 0.5) * 255
    spec = spec.astype(np.uint8)
    spec = np.tile(spec[:, :, np.newaxis], (1, 1, 3))

    img = Image.fromarray(spec)
    
    # img.save('melspectrogram.png')
    return img

