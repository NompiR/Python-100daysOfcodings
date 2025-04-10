import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
student_score = {student: random.randint(1, 100) for student in names}
print(student_score)
passed_students = {stud_name: score for (stud_name, score) in student_score.items() if score >= 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(' ')}
print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: round((temp_c * 9/5) + 32, 2) for (day, temp_c) in weather_c.items()}

print(weather_f)
