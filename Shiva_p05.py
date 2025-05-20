import matplotlib.pyplot as plt

# دسته‌بندی داده‌ها بر اساس ۴ بازه زمانی
labels = ["بازه اول", "بازه دوم", "بازه سوم", "بازه چهارم"]
counts = [1, 3, 3, 2]  # تعداد مفاهیم در هر بازه

# رسم نمودار میلهای
plt.figure(figsize=(8, 5))
plt.bar(labels, counts, color=['blue', 'green', 'orange', 'red'])
plt.xlabel("بازه‌های زمانی")
plt.ylabel("تعداد مفاهیم")
plt.title("نمودار میلهای مفاهیم در بازه‌های زمانی")
plt.show()

#Shiva_Hajalizadeh