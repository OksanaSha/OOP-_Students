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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.find_average()}'
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

cool_reviewer = Reviewer('Some', 'Buddy')

# print(cool_reviewer)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']

cool_lecture = Lecture('Some', 'Buddy')
cool_lecture.courses_attached += ['Python']
cool_lecture.courses_attached += ['C++']

best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'C++', 8)

print(cool_lecture)