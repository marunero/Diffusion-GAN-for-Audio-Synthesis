import librosa
import numpy as np
from PIL import Image

import argparse
import soundfile as sf

#########################################################################
#######################  melspectrogram -> audio  #######################  

def main(args):
    t = Image.open(args['input']).convert("L")
    t = t.resize((87, 87))
    t = np.array(t)

    t = t / 255.0
    t -= 0.5
    t *= 10
    t = 10 ** t

    res = librosa.feature.inverse.mel_to_audio(t, sr=22050, n_fft=1024, hop_length=256, win_length=1024, window = 'hann', center = True, pad_mode = 'reflect', power = 2.0, n_iter = 87)

    sf.write(args['save'], res, 22050)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--save", help="audio save path", default="output.wav")
    parser.add_argument("-i", "--input", help="input melspectrogram path", default="input.png")

    args = vars(parser.parse_args())

    main(args)