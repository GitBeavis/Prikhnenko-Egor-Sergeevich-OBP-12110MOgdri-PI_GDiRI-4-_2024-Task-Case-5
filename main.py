from student import Student


def main():
    students = [
        Student('Никита Астафьев', 20, 9.2, 3, 'Информатика', debt_count=3, threshold=1),
        Student('Мария Петрова', 22, 7.5, 2, 'Физика', debt_count=3),
        Student('Глеб Сергеев', 19, 5.0, 1, 'Математика', debt_count=8)
    ]

    for i, student in enumerate(students, 1):
        print(f'Информация о студенте {i}:\n{student}\n')


if __name__ == "__main__":
    main()
