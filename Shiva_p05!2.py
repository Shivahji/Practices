import matplotlib.pyplot as plt

# داده‌های دسته‌بندی‌شده
labels = ["بازه اول", "بازه دوم", "بازه سوم", "بازه چهارم"]
counts = [1, 3, 3, 2]  # تعداد مفاهیم در هر بازه

# رسم نمودار دایره‌ای
plt.figure(figsize=(6, 6))
plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=['blue', 'green', 'orange', 'red'])
plt.title("نمودار دایره‌ای مفاهیم در بازه‌های زمانی")
plt.show()