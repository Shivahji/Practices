import numpy as np
import matplotlib.pyplot as plt

# مقداردهی متغیرها
x = np.linspace(-1, 1, 100)
y1 = np.sin(x)
y2 = 2 * np.sin(x) * (np.cos(4)**2) - 2 * np.sin(-x) * (np.sin(2)**2)

# ایجاد نمودار ترکیبی
plt.figure(figsize=(6, 4))
plt.plot(x, y1, color='blue', linewidth=2, label=r'$y = \sin(x)$')
plt.plot(x, y2, color='red', linewidth=2, label=r'$y = 2 \sin(x) \cos^2(4) - 2 \sin(-x) \sin^2(2)$')

# تنظیمات نمودار
plt.xlabel("X")
plt.ylabel("Y")
plt.title("نمودار ترکیبی دو تابع")
plt.legend()
plt.grid()

# ذخیره تصویر در دو وضوح مختلف
plt.savefig("combined_plot.png", dpi=300)
plt.savefig("combined_plot_highres.png", dpi=600)

# نمایش نمودار
plt.show()

#Shiva_Hajalizadeh