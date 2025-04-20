# اطلاعات فایل "Info.txt"
file_content = {
    "First Name": "Shiva",
    "Last Name": "Hajalizadeh",
    "Student ID": "4032013056",
    "Birth Year": 2004,
    "Age": 20,
    "Favorite Movie": "war",
    "Favorite Band": "novan",
    "Field of Study": "Electerical Engineering",
    "Level of Education": "bachelor",
    "Graduation Year": 2022,
    "GPA": 21.5,
    "Skills": ["power lifting", "robotic"],
    "Hobbies": ["playing game", "badminton"],
    "Current Role": "student",
    "Strengths": ["Teamwork", "exercise"],
    "Weaknesses": ["Public speaking"],
    "Favorite Book": "chemistry",
    "Programming Languages": ["Python", "C+"],
    "Languages Known": ["English", "Turkish"],
    "Previous Experience": ["Bodybuilding"],
    "Job Experience": "Work in the company",
    "Support System": "Supportive and knowledgeable"
}

# نمایش دیکشنری اطلاعات
for key, value in file_content.items():
    print(f"{key}: {value}")
