# -*- coding: utf-8 -*-
import pyaudio
import numpy as np
from scipy import fftpack
import wave
###
import time
import struct
import math


def recording(filename, time=0, threshold=7000):
    """
    :param filename: 文件名
    :param time: 录音时间,如果指定时间，按时间来录音，默认为自动识别是否结束录音
    :param threshold: 判断录音结束的阈值
    :return:
    """
    CHUNK = 1024  # 块大小
    FORMAT = pyaudio.paInt16  # 每次采集的位数
    CHANNELS = 1  # 声道数
    RATE = 16000  # 采样率：每秒采集数据的次数
    RECORD_SECONDS = time  # 录音时间
    WAVE_OUTPUT_FILENAME = filename  # 文件存放位置
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)
    print("* 录音中...")
    frames = []
    if time > 0:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
    else:
        stopflag = 0
        stopflag2 = 0
        while True:
            data = stream.read(CHUNK)
            rt_data = np.frombuffer(data, np.dtype('<i2'))
            # print(rt_data*10)
            # 傅里叶变换
            fft_temp_data = fftpack.fft(
                rt_data, rt_data.size, overwrite_x=True)
            fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]

            # 测试阈值，输出值用来判断阈值
            # print(sum(fft_data) // len(fft_data))

            # 判断麦克风是否停止，判断说话是否结束，# 麦克风阈值，默认7000
            if sum(fft_data) // len(fft_data) > threshold:
                stopflag += 1
            else:
                stopflag2 += 1
            oneSecond = int(RATE / CHUNK)
            if stopflag2 + stopflag > oneSecond:
                if stopflag2 > oneSecond // 3 * 2:
                    break
                else:
                    stopflag2 = 0
                    stopflag = 0
            frames.append(data)
    print("* 录音结束")
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))


###
# 计算当前音频声音
swidth = 2
SHORT_NORMALIZE = (1.0/32768.0)


def rms(frame):
    count = len(frame) / swidth
    format = "%dh" % (count)
    shorts = struct.unpack(format, frame)

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)
        return rms * 1000


def rec(file_name):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    MAX_RECORD_SECONDS = 8
    TIMEOUT_LENGTH = 2  # 音量小于一定时间后停止录音

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音...")

    frames = []

    endTime = time.time() + MAX_RECORD_SECONDS  # 超过此时间自动停止
    lastTime = time.time()

    while True:
        if lastTime < endTime:

            input = stream.read(CHUNK)
            frames.append(input)

            # 声音大小，小于音量后超过多少秒停止 / 超过多长时间停止
            rms_val = rms(input)  # 当前音量

            if rms_val > 1:  # 如果说话了（音量大于 1）就更新时间
                lastTime = time.time()

            if time.time() - lastTime > TIMEOUT_LENGTH:     # 超过一定时间不说话，停止录音
                break

        else:   # 超时停止
            break

    print("录音结束")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    wf.close()
    print("保存文件成功")


recording('ppp.mp3', time=5)  # 按照时间来录音，录音5秒
# recording('ppp1.mp3')  # 没有声音自动停止，自动停止

# rec('ttt.mp3')