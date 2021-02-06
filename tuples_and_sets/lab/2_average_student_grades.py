n_students = int(input())

students_record = {}

for _ in range(n_students):

    name, grade = input().split()
    grade = float(grade)

    if name not in students_record:
        students_record[name] = [grade]
    else:
        students_record[name].append(float(grade))

for (name, grade) in students_record.items():
    avg_grade = sum(grade) / len(grade)
    grade_string = ' '.join(f'{g:.2f}' for g in grade)
    print(f'{name} -> {grade_string} (avg: {avg_grade:.2f})')


'''
7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00
'''