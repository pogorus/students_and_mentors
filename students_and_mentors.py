class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self):
        grade_summary = 0
        count = 0
        for course_grades in self.grades.values():
            for grade in course_grades:
                grade_summary += grade
                count += 1
        return grade_summary / count

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_rating()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.average_rating() < other.average_rating()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.average_rating() <= other.average_rating()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.average_rating() == other.average_rating()

    def __ne__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.average_rating() != other.average_rating()


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (self.courses_in_progress or self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        grade_summary = 0
        count = 0
        for course_grades in self.grades.values():
            for grade in course_grades:
                grade_summary += grade
                count += 1
        return grade_summary / count

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.average_rating() < other.average_rating()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.average_rating() <= other.average_rating()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.average_rating() == other.average_rating()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.average_rating() != other.average_rating()


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
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


first_student = Student('Bart', 'Simpson', 'male')
second_student = Student('Lisa', 'Simpson', 'female')

first_lecturer = Lecturer('Homer', 'Simpson')
second_lecturer = Lecturer('Marge', 'Simpson')

first_reviewer = Reviewer('Abraham', 'Simpson')
second_reviewer = Reviewer('Mona', 'Simpson')

first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Java']

second_student.courses_in_progress += ['Java']

first_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Java']

first_lecturer.courses_attached += ['Java']
second_lecturer.courses_attached += ['Python']

first_reviewer.rate_hw(first_student, 'Python', 3)
second_reviewer.rate_hw(first_student, 'Java', 2)
second_reviewer.rate_hw(second_student, 'Java', 9)

first_student.rate_hw(first_lecturer, 'Java', 1)
first_student.rate_hw(second_lecturer, 'Python', 8)
second_student.rate_hw(first_lecturer, 'Java', 7)

print(first_student)

print(second_lecturer)

print(first_reviewer)

print(first_student <= second_student)

print(first_lecturer == second_lecturer)

def average_student_rating_by_course(course, *students):
    grade_summary = 0
    count = 0

    for student in students:
        if course in (student.courses_in_progress or student.finished_courses):
            for grade in student.grades[course]:
                grade_summary += grade
                count += 1
    return grade_summary / count

print(average_student_rating_by_course('Java', first_student, second_student))
print(average_student_rating_by_course('Python', first_student, second_student))

def average_lecturer_rating_by_course(course, *lecturers):
    grade_summary = 0
    count = 0

    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            for grade in lecturer.grades[course]:
                grade_summary += grade
                count += 1
    return grade_summary / count

print(average_lecturer_rating_by_course('Java', first_lecturer, second_lecturer))