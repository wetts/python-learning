# -*- encoding: utf-8 -*-
'''
@File    :   librosa_test.py
@Time    :   2019/11/27 13:37:33
@Author  :   Zhang Wensong
@Version :   1.0
@Contact :   zhang.wetts@163.com
@Desc    :   librosa test
'''

# here put the import lib
import librosa
import pyaudio
# import wave
from pydub import AudioSegment

wave_path = './1.mp3'
y, sr = librosa.load(wave_path, sr=None)
song = AudioSegment.from_mp3(wave_path)
# wf = wave.open(wave_path, 'rb')

print(y)
# print(wf)
print(song)
