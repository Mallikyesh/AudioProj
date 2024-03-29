import pandas as pd 
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

from glob import glob
import librosa
import librosa.display
import IPython.display as ipd

from itertools import cycle

sns.set_theme(style="white" , palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle=cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])
audio_files =glob('eee.wav')
ipd.Audio(audio_files[0])

y, sr = librosa.load(audio_files[0])
print(f'y:{y[:10]}')

print(f'shape y: {y.shape}')
print(f'sr: {sr}')

pd.Series(y).plot(figsize=(10,5), lw=1, title='Raw Audio Example my first audio proj',color=color_pal[0])
D=librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
S_db.shape

fig, ax=plt.subplots(figsize=(10,5))
img = librosa.display.specshow(S_db,x_axis='time',y_axis='log',ax=ax)


plt.show()


