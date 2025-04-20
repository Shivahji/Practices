# متن دریافتی به صورت ثابت
received_message = """You have a new website form submission
1.First Name: Alex
2.Email Address: karen.ignaci5656@yahoo.com
3.Phone Number: 23866905544
4.Message: Hello, I have a question."""

# متن پیام ارسالی اولیه
response_template = "Dear NAME, thank you for reaching out to our company.\nWe appreciate your interest and are excited to explore how we can support your needs."

# استخراج نام کاربر از متن دریافتی
def extract_name(received_message):
    lines = received_message.splitlines()
    for line in lines:
        if "First Name:" in line:
            name = line.split(":")[1].strip()
            return name
    return "User"  # پیش‌فرض، اگر نام پیدا نشود

# جایگذاری نام کاربر در متن پیام ارسالی
def create_response(name, response_template):
    return response_template.replace("NAME", name)

# پردازش پیام
user_name = extract_name(received_message)
response_message = create_response(user_name, response_template)

# نمایش پیام نهایی
print(response_message)
