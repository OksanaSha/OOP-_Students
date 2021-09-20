class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_in_progress and course in lecture.courses_attached:
            lecture.grades[course] = lecture.grades.get(course, []) + [grade]
        else:
            print(f'Оценка не засчитана. Курс {course} недоступен для студента/лектора.')
            return 'Ошибка'

    def find_average_hw(self):
        total_grades = 0
        count_grades = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count_grades += len(grades)
        return total_grades / count_grades

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.find_average_hw()}\n' \
              f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {" ".join(self.finished_courses)}\n' \
              f'\n'
        return res

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.find_average_hw() < other.find_average_hw()
        else:
            return 'Ошибка'

    def __eq__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.find_average_hw() == other.find_average_hw()
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def find_average(self):
        total_grades = 0
        count_grades = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count_grades += len(grades)
        return total_grades / count_grades

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.find_average()}' \
              f'\n'
        return res

    def __lt__(self, other):
        if isinstance(self, Lecture) and isinstance(other, Lecture):
            return self.find_average() < other.find_average()
        else:
            return 'Ошибка'

    def __eq__(self, other):
        if isinstance(self, Lecture) and isinstance(other, Lecture):
            return self.find_average() == other.find_average()
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print(f'Оценка не засчитана. Курс {course} недоступен для студента/проверяющего.')
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}' \
              f'\n'
        return res

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']

# print(cool_reviewer)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Java']

other_student = Student('Alex', 'VV', 'your_gender')
other_student.courses_in_progress += ['C++']
other_student.finished_courses += ['Python']
other_student.finished_courses += ['Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Java', 8)
cool_reviewer.rate_hw(best_student, 'C++', 9)
cool_reviewer.rate_hw(other_student, 'C++', 5)


# print(best_student)

cool_lecture = Lecture('Some', 'Buddy')
cool_lecture.courses_attached += ['Python']
cool_lecture.courses_attached += ['C++']

other_lecture = Lecture('New', 'Buddy')
other_lecture.courses_attached += ['Python']
other_lecture.courses_attached += ['C++']

best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'C++', 8)
best_student.rate_lecture(other_lecture, 'Python', 9)
best_student.rate_lecture(other_lecture, 'Python', 7)
best_student.rate_lecture(other_lecture, 'Python', 10)

print(cool_lecture > other_lecture)
print(cool_lecture != other_lecture)
