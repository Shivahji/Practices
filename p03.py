import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# فایل صوتی را بخوانید
file_name = "sample.wav"  # نام فایل را در صورت نیاز تغییر دهید
data, sample_rate = sf.read(file_name)

# محاسبه FFT
N = len(data)  # تعداد نمونه‌ها
fft_data = np.fft.fft(data)
frequencies = np.fft.fftfreq(N, d=1/sample_rate)

# یافتن بیشینه فرکانس
dominant_freq = abs(frequencies[np.argmax(abs(fft_data))])

# نمایش نتایج
print(f"Sample Rate: {sample_rate} Hz")
print(f"Dominant Frequency: {dominant_freq:.2f} Hz")

# رسم نمودار طیف فرکانسی
plt.figure(figsize=(10, 5))
plt.plot(frequencies[:N//2], abs(fft_data[:N//2]))  # فقط نصف فرکانس‌ها را نمایش می‌دهیم
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT Spectrum")
plt.show()

#Shiva_Hajalizadeh