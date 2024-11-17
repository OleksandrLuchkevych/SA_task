from tree import *

def build_clinic_hierarchy():
    # Кореневий вузол дерева
    root = TreeNode(1, "Основна мета: Реалізувати інформаційну систему керування клінікою")

    # F1: Управління пацієнтами
    F1 = TreeNode(2, "F1: Управління пацієнтами")
    root.add_child(F1)

    # K1: Облік медичної інформації пацієнтів
    K1 = TreeNode(3, "K1: Облік медичної інформації пацієнтів")
    F1.add_child(K1)
    for i, system in enumerate(["Microsoft Access", "MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=4):
        K1.add_child(TreeNode(i, f"A{i-3}: {system}"))

    # K2: Доступ до історії лікувань
    K2 = TreeNode(8, "K2: Доступ до історії лікувань")
    F1.add_child(K2)
    for i, system in enumerate(["Microsoft Access", "MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=9):
        K2.add_child(TreeNode(i, f"A{i-8}: {system}"))

    # K3: Планування візитів і нагадування
    K3 = TreeNode(13, "K3: Планування візитів і нагадування")
    F1.add_child(K3)
    for i, system in enumerate(["Microsoft Access", "MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=14):
        K3.add_child(TreeNode(i, f"A{i-13}: {system}"))

    # F2: Фінансове управління
    F2 = TreeNode(18, "F2: Фінансове управління")
    root.add_child(F2)

    # K4: Облік платежів
    K4 = TreeNode(19, "K4: Облік платежів")
    F2.add_child(K4)
    for i, system in enumerate(["Microsoft Access", "MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=20):
        K4.add_child(TreeNode(i, f"A{i-19}: {system}"))

    # K5: Генерація фінансових звітів
    K5 = TreeNode(24, "K5: Генерація фінансових звітів")
    F2.add_child(K5)
    for i, system in enumerate(["Microsoft Access", "MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=25):
        K5.add_child(TreeNode(i, f"A{i-24}: {system}"))

    # F3: Управління ресурсами клініки
    F3 = TreeNode(29, "F3: Управління ресурсами клініки")
    root.add_child(F3)

    # K6: Управління матеріалами
    K6 = TreeNode(30, "K6: Управління матеріалами")
    F3.add_child(K6)
    for i, system in enumerate(["MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=31):
        K6.add_child(TreeNode(i, f"A{i-30}: {system}"))

    # K7: Управління графіками лікарів
    K7 = TreeNode(34, "K7: Управління графіками лікарів")
    F3.add_child(K7)
    for i, system in enumerate(["MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=35):
        K7.add_child(TreeNode(i, f"A{i-34}: {system}"))

    return root


# Приклад використання програми
if __name__ == "__main__":
    clinic_hierarchy = build_clinic_hierarchy()

    # Виведення дерева
    print("Структура дерева:")
    clinic_hierarchy.print_tree()

    # Пошук вузла за ID через термінал
    while True:
        try:
            user_input = input("\nВведіть номер вузла для пошуку (або 'exit' для виходу): ").strip()
            if user_input.lower() == 'exit':
                print("Завершення програми.")
                break

            target_number = int(user_input)
            node = clinic_hierarchy.navigate(target_number)
            if node:
                print(f"Знайдений вузол: {node.number}: {node.name}")
            else:
                print("Вузол з таким номером не знайдено.")
        except ValueError:
            print("Будь ласка, введіть коректне число або 'exit' для виходу.")