students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
ortacha_baho = sum(students.values()) / len(students)
print("O'rtacha baho:", ortacha_baho)
print("O'rtacha balldan yuqori baho olgan talabalar:")
for student, baho in students.items():
    if baho > ortacha_baho:
        print(ortacha_baho,"dan yuqori:", student)