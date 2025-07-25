students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]
eng_qisq_ism = min(students, key= lambda a :len(a["name"]))
print("Eng qisqa ism :", eng_qisq_ism["name"])