class Student:
    # Конструктор, инициализируем свойства
    def __init__(
            self,
            full_name: str,
            age: int,
            average_grade: float,
            year: int,
            faculty: str,
            debt_count: int = 0,
            threshold: int = 3
    ):
        """
        Студент вуза
        :param full_name: ФИО полностью
        :param age: Возраст
        :param average_grade: Средняя оценка по предметам
        :param year: Год обучения (Номер курса)
        :param faculty: Факультет
        :param debt_count: Количество долгов по предметам
        :param threshold: Максимально допустимое количество долгов
        """
        self.full_name = full_name
        self.age = age
        self.average_grade = average_grade
        self.year = year
        self.faculty = faculty
        self.debt_count = debt_count
        self.is_candidate_for_dismissal = False  # Флаг на отчисление
        self.check_for_dismissal(threshold)

    # Методы установки и получения значений для каждого свойства
    # Смысла в Python не имеют из-за отсутствия сокрытия
    # Написаны в рамках тех. задания
    def set_full_name(self, full_name: str) -> None:
        self.full_name = full_name

    def get_full_name(self) -> str:
        return self.full_name

    def set_age(self, age: int) -> None:
        self.age = age

    def get_age(self) -> int:
        return self.age

    def set_average_grade(self, average_grade: float) -> None:
        self.average_grade = average_grade

    def get_average_grade(self) -> float:
        return self.average_grade

    def set_year(self, year: int) -> None:
        self.year = year

    def get_year(self) -> int:
        return self.year

    def set_faculty(self, faculty: str) -> None:
        self.faculty = faculty

    def get_faculty(self) -> str:
        return self.faculty

    def set_debt_count(self, debt_count: int) -> None:
        self.debt_count = debt_count

    def get_debt_count(self) -> int:
        return self.debt_count

    # Метод для оценки успеваемости студента на основе среднего балла
    def evaluate_performance(self) -> str:
        if self.average_grade > 8:
            return 'Отлично'
        elif self.average_grade >= 6:
            return 'Хорошо'
        elif self.average_grade >= 4:
            return 'Удовлетворительно'
        else:
            return 'Неудовлетворительно'

    # Метод для генерации уникального ID студента
    def generate_id(self) -> str:
        # Извлекаем первую букву имени и фамилии
        name_parts = self.full_name.split()
        if len(name_parts) >= 2:
            initials = name_parts[0][0].upper() + name_parts[1][0].upper()
        else:
            # Если имя не содержит фамилии, используем первую букву одного слова
            initials = name_parts[0][0].upper()
        return f'{initials}{self.faculty[0].upper()}{self.year}'

    # Метод для проверки на отчисление, если количество долгов больше порога
    def check_for_dismissal(self, threshold: int):
        if self.debt_count > threshold:
            self.is_candidate_for_dismissal = True
        else:
            self.is_candidate_for_dismissal = False

    # Информация о студенте
    def __str__(self):
        return f'Имя: {self.full_name}\n' \
               f'Возраст: {self.age}\n' \
               f'Средний балл: {self.average_grade}\n' \
               f'Курс: {self.year}\nФакультет: {self.faculty}\n' \
               f'Долгов по предметам: {self.debt_count}\n' \
               f'Оценка успеваемости: {self.evaluate_performance()}\n' \
               f'ID студента: {self.generate_id()}\n' \
               f'Кандидат на отчисление: {"Да" if self.is_candidate_for_dismissal else "Нет"}\n'
