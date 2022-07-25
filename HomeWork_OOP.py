class Student:
    def __init__(self, name, surname, gender):
        self.average_homework = None
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw(self):
        count = 0
        for key in self.grades:
            count += len(self.grades[key])
        self.average_homework = round((sum(map(sum, self.grades.values())) / count), 1)
        return self.average_homework

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Запрашиваемый студент отсутствует')
            return
        return self.average_hw() < other.average_hw()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за лекции: {self.average_hw()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_grades = None

    def average_rating(self):
        count = 0
        for key in self.grades:
            count += len(self.grades[key])
        self.average_grades = round((sum(map(sum, self.grades.values())) / count), 1)
        return self.average_grades

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Запрашиваемый лектор отсутствует')
            return
        return self.average_rating() > other.average_rating()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за лекции: {self.average_rating()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def average_student_grade():
    all_students_grades = []
    for x in students:
        for key, value in x.grades.items():
            if key == 'Python':
                for y in value:
                    all_students_grades.append(y)
    average_student_grade = round(sum(all_students_grades) / len(all_students_grades), 1)
    print(f'Средняя оценка всех студентов курса "Python": {average_student_grade}')


def average_lecturer_grade():
    all_lecturer_grades = []
    for x in lecturers:
        for key, value in x.grades.items():
            if key == 'Git':
                for y in value:
                    all_lecturer_grades.append(y)
    average_lecturer_grade = round(sum(all_lecturer_grades) / len(all_lecturer_grades), 1)
    print(f'Средняя оценка всех лекторов курса "Python": {average_lecturer_grade}')


lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python']
lecturer.courses_attached += ['Git']

lecturer_2 = Lecturer('Old', 'Fashion')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

student = Student('Ruoy', 'Eman', 'M')
student.courses_in_progress += ['Python']
student.courses_in_progress += ['Git']
student.finished_courses += ['Введение в программирование']
student.rate_l(lecturer, 'Python', 2)
student.rate_l(lecturer, 'Python', 2)
student.rate_l(lecturer, 'Git', 5)
student.rate_l(lecturer, 'Git', 5)

student_2 = Student('Joan', 'Green', 'W')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в програмирование']
student_2.rate_l(lecturer_2, 'Python', 8)
student_2.rate_l(lecturer_2, 'Python', 8)
student_2.rate_l(lecturer_2, 'Git', 5)
student_2.rate_l(lecturer_2, 'Git', 5)

reviewer = Reviewer('Bugs', 'Bunny')
reviewer.courses_attached += ['Python']
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 10)

reviewer_2 = Reviewer('Terry', 'Jons')
reviewer_2.courses_attached += ['Git']
reviewer_2.rate_hw(student, 'Git', 8)
reviewer_2.rate_hw(student, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 8)

students = [student, student_2]
lecturers = [lecturer, lecturer_2]

print("Студенты:")
print(student)
print()
print(student_2)
print()
print("Проверяющие:")
print(reviewer)
print()
print(reviewer_2)
print()
print("Лекторы:")
print(lecturer)
print()
print(lecturer_2)
print()
average_student_grade()
average_lecturer_grade()
print()
print(student > student_2)
print(lecturer < lecturer_2)
