# 内插与抽取可以用scipy库中的interpolate模块实现
import numpy as np
from scipy import interpolate

# 实现内插，输入为原始数据，原始采样率，新的采样率
def interp(data, rate, new_rate):
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
def downsample(data, rate, new_rate):
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