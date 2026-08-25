class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (
                isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
                and 1 <= grade <= 10
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade():.1f}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_grade():.1f}'
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
                isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress
                and 1 <= grade <= 10
        ):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_hw_grade_for_course(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    if len(all_grades) == 0:
        return 0
    return sum(all_grades) / len(all_grades)


def average_lecture_grade_for_course(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if len(all_grades) == 0:
        return 0
    return sum(all_grades) / len(all_grades)


student_1 = Student('Ольга', 'Алёхина', 'Ж')
student_2 = Student('Анна', 'Смирнова', 'Ж')

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Пётр', 'Петров')

reviewer_1 = Reviewer('Сергей', 'Сергеев')
reviewer_2 = Reviewer('Мария', 'Орлова')

student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['Введение в программирование']

lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'Java']

reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)

reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Git', 9)

student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Java', 7)

students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]

print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print(student_1 < student_2)
print(lecturer_1 < lecturer_2)
print()
print(average_hw_grade_for_course(students_list, 'Python'))
print(average_lecture_grade_for_course(lecturers_list, 'Python'))