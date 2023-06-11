import librosa
import numpy as np
from diffwave.params import params
from PIL import Image

#########################################################################
#######################  melspectrogram -> audio  #######################  

def mel2wav(mel_png):
    t = Image.open(mel_png)).convert("L")
    t = t.resize((87, 87))
    t = np.array(t)

    t = t / 255.0
    t -= 0.5
    t *= 10
    t = 10 ** t

    res = librosa.feature.inverse.mel_to_audio(t, sr=22050, n_fft = params.n_fft, hop_length = params.hop_samples, win_length = params.hop_sample * 4, window = 'hann', center = True, pad_mode = 'reflect', power = 2.0, n_iter = 87)

    import soundfile as sf
    sf.write("result.wav", res, 22050)
