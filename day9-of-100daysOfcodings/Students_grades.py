student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for i in student_scores:
    s = student_scores[i]

    if s >= 91:
        student_grades[i] = "Outstanding"
    elif s >= 81:
        student_grades[i] = "Exceeds Expectations"
    elif s >= 71:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"
        
count = 0
for key, val in student_grades.items():
    count += 1
    print(f"{count}) {key}  ---> {val}")


