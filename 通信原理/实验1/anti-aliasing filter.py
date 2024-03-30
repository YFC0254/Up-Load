from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
"""
低通滤波器的通带通常定义为从直流（0 Hz）开始，一直到截止频率。截止频率通常定义为信号通过滤波器时幅度衰减为原来的1/sqrt(2) (约-3dB)的频率。阻带则是滤波器消除或减少的频率范围。对于低通滤波器，阻带通常是从截止频率以上的频率开始。
"""
# Butterworth低通滤波器设计
def design_lowpass_filter(cutoff_frequency, sample_rate, filter_order):#输入截止频率，采样频率，滤波器阶数
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
def apply_lowpass_filter(data, cutoff_frequency, sample_rate, filter_order):#输入数据，截止频率，采样频率，滤波器阶数
    b, a = design_lowpass_filter(cutoff_frequency, sample_rate, filter_order)
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data #返回滤波后的数据
