class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        Student.all_students.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture):
            if course not in self.courses_in_progress:
                print(f'Оценка не засчитана. Курс {course} недоступен для студента {self.name}')
            elif course not in lecture.courses_attached:
                print(f'Оценка не засчитана. Курс {course} недоступен для лектора {lecture.name}')
            else:
                lecture.grades[course] = lecture.grades.get(course, []) + [grade]
        else:
            print('Ошибка')



    def find_average_course(self, course):
        if self.grades.get(course):
            res = sum(self.grades[course]) / len(self.grades[course])
            return round(res, 2)
        return 'Ошибка'

    def find_average_hw(self):
        total_grades = 0
        for course in self.grades.keys():
            total_grades += self.find_average_course(course)
        res = total_grades / len(self.grades)
        return round(res, 2)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.find_average_hw()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n' \
              f'\n'
        return res

    def __lt__(self, other):
        return self.find_average_hw() < other.find_average_hw()

    def __eq__(self, other):
        return self.find_average_hw() == other.find_average_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    all_lectures = []

    def __init__(self, name, surname):
        Lecture.all_lectures.append(self)
        super().__init__(name, surname)
        self.grades = {}

    def find_average_course(self, course):
        if self.grades.get(course):
            res = sum(self.grades[course]) / len(self.grades[course])
            return round(res, 2)
        return 'Ошибка'

    def find_average_lec(self):
        total_grades = 0
        for course in self.grades.keys():
            total_grades += self.find_average_course(course)
        res = total_grades / len(self.grades)
        return round(res, 2)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.find_average_lec()}\n' \
              f'\n'
        return res

    def __lt__(self, other):
        return self.find_average_lec() < other.find_average_lec()

    def __eq__(self, other):
        return self.find_average_lec() == other.find_average_lec()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course not in self.courses_attached:
                print(f'Оценка не засчитана. Курс {course} недоступен для проверяющего {self.name}')
            elif course not in student.courses_in_progress:
                print(f'Оценка не засчитана. Курс {course} недоступен для студента {student.name}')
            else:
                student.grades[course] = student.grades.get(course, []) + [grade]
        else:
            print('Ошибка')

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}' \
              f'\n'
        return res


def find_average_students(all_students, course):
    '''
    Find course average hw for all students
    :param all_students: students list
    :param course: course name
    :return: average
    '''
    total_grades = 0
    count_grades = 0
    for student in all_students:
        if course in student.courses_in_progress:
            total_grades += student.find_average_course(course)
            count_grades += 1
        if count_grades == 0:
            return 'Невозможно посчитать средний балл'
    return round(total_grades / count_grades, 2)
    # Вариант 2
    # Если среднее от среднего не подходит
    # total_grades = 0
    # count_grades = 0
    # for student in all_students:
    #     if course in student.courses_in_progress:
    #         total_grades += sum(student.grades[course])
    #         count_grades += len(student.grades[course])
    #     if count_grades == 0:
    #         return 'Невозможно посчитать средний балл'
    # return total_grades / count_grades

def find_average_lectures(all_lectures, course):
    '''
    Find course average lecture for all lectures
    :param all_lectures: lectures list
    :param course: course name
    :return: average
    '''
    total_grades = 0
    count_grades = 0
    for lecture in all_lectures:
        if course in lecture.courses_attached:
            total_grades += lecture.find_average_course(course)
            count_grades += 1
        if count_grades == 0:
            return 'Невозможно посчитать средний балл'
    return round(total_grades / count_grades, 2)
    # Вариант 2
    # Если среднее от среднего не подходит
    # total_grades = 0
    # count_grages = 0
    # for lecture in all_lectures:
    #     if course in lecture.courses_attached:
    #         total_grades += sum(lecture.grades[course])
    #         count_grages += len(lecture.grades[course])
    #     if count_grages == 0:
    #         return 'Невозможно посчитать средний балл'
    # return total_grades / count_grades

cool_reviewer = Reviewer('Super', 'Man')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++', 'C#']

other_reviewer = Reviewer('New', 'Man')
other_reviewer.courses_attached += ['Java', 'Python', 'C++']

best_student = Student('Ruoy', 'Eman', 'm')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++', 'Java']
best_student.finished_courses += ['C#']

other_student = Student('Alex', 'VV', 'm')
other_student.courses_in_progress += ['C++', 'C#']
other_student.finished_courses += ['Python']
other_student.finished_courses += ['Java']

cool_lecture = Lecture('James', 'Bond')
cool_lecture.courses_attached += ['Python']
cool_lecture.courses_attached += ['C++', 'C#']

other_lecture = Lecture('Mister', 'X')
other_lecture.courses_attached += ['Python']
other_lecture.courses_attached += ['Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 8)
cool_reviewer.rate_hw(best_student, 'C++', 9)
cool_reviewer.rate_hw(other_student, 'C#', 5)
cool_reviewer.rate_hw(other_student, 'C++', 8)

other_reviewer.rate_hw(best_student, 'Python', 7)
other_reviewer.rate_hw(best_student, 'Java', 5)
other_reviewer.rate_hw(best_student, 'C++', 8)
other_reviewer.rate_hw(other_student, 'Java', 10)
other_reviewer.rate_hw(other_student, 'C++', 4)

best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'C++', 8)
best_student.rate_lecture(other_lecture, 'Python', 10)
best_student.rate_lecture(other_lecture, 'Python', 9.5)
best_student.rate_lecture(other_lecture, 'Java', 7)

other_student.rate_lecture(cool_lecture, 'C++', 10)
other_student.rate_lecture(cool_lecture, 'C#', 6)
other_student.rate_lecture(cool_lecture, 'C++', 8)
other_student.rate_lecture(other_lecture, 'C#', 10)

print(other_student.find_average_course('Java'))
print(best_student.find_average_course('Java'))
print(best_student.find_average_course('Bla-bla'))
print()

print(cool_lecture.find_average_lec())
print(other_lecture.find_average_course('C#'))
print(other_lecture.find_average_course('Python'))

# students_average = find_average_students(Student.all_students, course=input('Введите название курса: '))
# print(f'Средняя оценка за домашние задания у студентов по данному курсу: {students_average}')
# print()
#
# lectures_average = find_average_lectures(Lecture.all_lectures, course=input('Введите название курса: '))
# print(f'Средняя оценка за занятия у лекторов данного курса: {lectures_average}')
# print()

print('\nСписок студентов:\n')
print(*Student.all_students, sep='')
print('Список лекторов:\n')
print(*Lecture.all_lectures, sep='')