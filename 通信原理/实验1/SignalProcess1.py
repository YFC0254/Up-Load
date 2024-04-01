import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy import interpolate

# 抗混叠滤波类
class AntiAliasingFilter:
    """
    低通滤波器的通带通常定义为从直流（0 Hz）开始，一直到截止频率。截止频率通常定义为信号通过滤波器时幅度衰减为原来的1/sqrt(2) (约-3dB)的频率。阻带则是滤波器消除或减少的频率范围。对于低通滤波器，阻带通常是从截止频率以上的频率开始。
    """
    # Butterworth低通滤波器设计
    def design_lowpass_filter(self, cutoff_frequency, sample_rate, filter_order):#输入截止频率，采样频率，滤波器阶数
        if not cutoff_frequency or not sample_rate or not filter_order:
            raise ValueError("cutoff_frequency, sample_rate, and filter_order must all be non-empty values")
        nyquist_rate = sample_rate / 2.0 #奈奎斯特频率
        normal_cutoff = cutoff_frequency / nyquist_rate #归一化截止频率
        b, a = signal.butter(filter_order, normal_cutoff, btype='low', analog=False)
        # 此时滤波器的通带增益为1，截止频率为1，截止频率处的增益为-3dB，截止频率处的相位为-45度，截止频率的相位延迟为1/4个周期
        # 计算此时的通带范围
        passband_range = [0, cutoff_frequency]
        # 计算阻带范围
        stopband_range = [cutoff_frequency, nyquist_rate]
        return b, a , passband_range, stopband_range #返回滤波器系数，通带范围，阻带范围

    # 应用滤波器
    def apply_lowpass_filter(self, data, cutoff_frequency, sample_rate, filter_order):#输入数据，截止频率，采样频率，滤波器阶数
        b, a = self.design_lowpass_filter(cutoff_frequency, sample_rate, filter_order)
        filtered_data = signal.filtfilt(b, a, data)
        return filtered_data #返回滤波后的数据

# 信号处理基础类
class BasicSignal:
    def __init__(self, data, rate):
        self.data = data
        self.rate = rate
    
    # 画出信号波形
    def draw(self,name,xlabel,ylabel):
        plt.figure (f'{name} wave')
        plt.plot(self.data)
        plt.title(f'{name}  wave')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
    
    # 画出功率谱
    def draw_psd(self,name):
        f, Pxx = signal.periodogram(self.data, self.rate)
        plt.figure (f'{name} psd')
        plt.plot(f, Pxx)
        plt.title(f'{name}  psd')
        plt.xlabel('frequency')
        plt.ylabel('power')
        plt.show()

# 内插采样类
class InterpolationDownsampling:
    # 内插与抽取可以用scipy库中的interpolate模块实现
    # 实现内插，输入为原始数据，原始采样率，新的采样率
    def interp(self,data, rate, new_rate):
        # 生成原始数据的时间序列
        time = np.linspace(0, len(data) / rate, len(data))
        # 生成新的时间序列
        new_time = np.linspace(0, len(data) / rate, int(len(data) * new_rate / rate))
        # 生成插值函数
        f = interpolate.interp1d(time, data)
        # 生成插值数据
        data_new = f(new_time)
        return data_new #返回新的插值数据

    # 实现抽取，输入为原始数据，原始采样率，新的采样率
    def downsample(self,data, rate, new_rate):
        # 生成原始数据的时间序列
        time = np.linspace(0, len(data) / rate, len(data))
        # 生成新的时间序列
        new_time = np.linspace(0, len(data) / rate, int(len(data) * new_rate / rate))
        # 生成插值函数
        f = interpolate.interp1d(time, data)
        # 生成插值数据
        data_new = f(new_time)
        # 生成抽取数据
        data_downsample = data_new[::int(rate / new_rate)]
        return data_downsample #返回新的抽取数据

