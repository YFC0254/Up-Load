import numpy as np
from scipy.io.wavfile import read

# 读取wav文件，得到采样率和数据
sample_rate, data = read('C:\\Users\\88486\\Desktop\\WorkSpace\\Python\\通信原理\\suno.wav') 
print(sample_rate,data)
# 创建载波信号
time = np.arange(len(data))/float(sample_rate)
carrier_freq=sample_rate*2
carrier = np.cos(2.0 * np.pi * carrier_freq * time)
# AM调制
modulated_data = carrier * data
# 你需要再将调制结果保存到新的wav文件中，可以使用scipy.io.wavfile.write