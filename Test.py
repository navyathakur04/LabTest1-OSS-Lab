import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
heart_rate_data=60 
HeartRate=np(0,1440,heart_rate_data)
def low_pass_filter(data, cutoff=0.01, order=3):
b, a = butter(order, cutoff, btype='low', analog=False)
return filtfilt(b, a, data)
noisy_heart_rate = low_pass_filter(heart_rate_data)
def compute_hourly_averages(data, minutes_per_hour=60):
hourly_averages = np.mean(data.reshape(-1, minutes_per_hour), axis=1)
return hourly_averages
plt.figure(figsize=(12, 6))
plt.plot(time, noisy_heart_rATE, label='Noisy heart rate', color='gray', alpha=0.6)
plt.plot(time, smoothed_DATA, label='Smoothed  Data', color='blue', linewidth=2)
plt.scatter(np.arange(24), hourly_averages, color='green', label='Hourly Averages', zorder=5)
plt.xlabel('Time (hours)')
plt.ylabel('HEART RATE')
plt.legend()
plt.grid(True)
plt.show()

