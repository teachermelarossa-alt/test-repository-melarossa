# test-repository-melarossa
Привет


1. Команда - 
1.1 Создать класс Person
__init__(self,name,age,sex)
1.2 Создать функцию - метод: introduce_person
p.introduce_person()
Человек <self.name>, возраст <self.age>,пол <self.sex>
1.3 Описать документацию - описать в доке что делает данная функция - описание 

2. Команда -
1.1 Создать класс Car
__init__(self,name,model,age)
1.2 Создать функцию introduce_car
Человек <self.name>, возраст <self.model>,пол <self.age>
1.3 Описать документацию - описать что делает данный класс

1. Команда номер 1:
Школа:
1. чел. - Student(атрибуты, name,grade)
Метод get_status() - Возвращает
отлично если оценка > 8 иначе 
Удовлетворительно
s = Student("ivan",7)
2. чел. - Teacher(атрибуты name,subject)
Метод teach - Возвращает:
Учитель self.name, преподает self.subject
t = Teacher("Mariya", "Math")
3. чел. - Classroom - атрибуты teacher, student
Метод lesson(self) 
Учитель <self.teacher.name> ведет урок у <self.stunent.name> оценка ученика <self.student.grade>
c = Classroom(s,t)

2. Команда Фитнесс-клуб:
1. Чел 1. - класс Exercise, атрибуты name, calories_per_min.
метод get_info - "Название self.name, Цена self.calories_per_min"
2. Чел 2. CardioSession - атрибуты exercise, duration.
метод burned_calories(self) - вычисляет цену калории.
self.exercise.calories_per_min * self.duration
3. Чел 3. Workout(cardio_session)
Метод total_calories(self) -  вызывает cardio_session.burned_calories()