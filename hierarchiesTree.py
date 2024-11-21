from tree import *

def build_clinic_hierarchy():
    # Кореневий вузол дерева
    root = TreeNode(1, "Основна мета: Реалізувати інформаційну систему керування клінікою")
    current_id = 2  # Початковий ID для нащадків

    # Критерій F1
    F1 = TreeNode(current_id, "F1: Управління пацієнтами")
    root.add_child(F1)
    current_id += 1

    # Додати 3 підкритерії до F1
    for criterion in [
        "K1: Облік медичної інформації пацієнтів",
        "K2: Доступ до історії лікувань",
        "K3: Планування візитів і нагадування"
    ]:
        sub_criterion = TreeNode(current_id, criterion)
        F1.add_child(sub_criterion)
        current_id += 1

        # Додавання 4 альтернатив
        for i, system in enumerate(["Microsoft Access", "MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=1):
            sub_criterion.add_child(TreeNode(current_id, f"A{i}: {system}"))
            current_id += 1

    # Критерій F2
    F2 = TreeNode(current_id, "F2: Фінансове управління")
    root.add_child(F2)
    current_id += 1

    # Додати 3 підкритерії до F2
    for criterion in [
        "K4: Облік платежів",
        "K5: Генерація фінансових звітів",
        "K6: Планування бюджету"
    ]:
        sub_criterion = TreeNode(current_id, criterion)
        F2.add_child(sub_criterion)
        current_id += 1

        # Додавання 4 альтернатив
        for i, system in enumerate(["Microsoft Access", "MySQL", "Хмарна платформа", "Спеціалізоване ПЗ"], start=1):
            sub_criterion.add_child(TreeNode(current_id, f"A{i}: {system}"))
            current_id += 1

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
