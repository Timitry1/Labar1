x = 0
groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Андрей",
        "surname": "Иванов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 2]
    },
    {
        "name": "Павел",
        "surname": "Андреев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [5, 3, 2]
    },
    {
        "name": "Павел",
        "surname": "Андреев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [5, 5, 2]
    },
]
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)

c = float(input("Введите значение среднего балла"))

def filtr_student(students):
    for student in students:
        x = float(sum(student["marks"]))
        y = float(len(student["marks"]))
        z =x/y
        if z >= c:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
filtr_student(groupmates)
