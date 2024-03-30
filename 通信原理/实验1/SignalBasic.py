# 导入库
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import scipy.signal as signal
import scipy.io as io

# 读取、画出信号波形和功率谱
# 读取语音信号
# win下读取wav文件
rate, data = wav.read('C:\\Users\\88486\\Desktop\\WorkSpace\\Up&Load\\通信原理\\suno.wav')

# 画出信号波形
def draw(data,name,rate,xlabel,ylabel):
    plt.figure (f'{name} wave')
    plt.plot(data)
    plt.title(f'{name}  wave')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


# 计算功率谱
"""
f:返回的频率数组;
Pxx:对应每个频率点的功率谱密度值。
"""
# 功率谱密度的英文名是Power Spectral Density，简称PSD
f, Pxx = signal.periodogram(data, rate)

# 公式计算功率谱:
data_FFT=np.fft.fft(data)
Pf=abs(data_FFT)**2/len(data)
f=np.linspace(0,rate,len(data))

# 画出功率谱
def draw_psd(data,name):
    f, Pxx = signal.periodogram(data, rate)
    plt.figure (f'{name} psd')
    plt.plot(f, Pxx)
    plt.title(f'{name}  psd')
    plt.xlabel('frequency')
    plt.ylabel('power')
    plt.show()
