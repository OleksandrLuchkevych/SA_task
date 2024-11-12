from tree import *

def build_clinic_hierarchy():
    # Кореневий вузол дерева
    root = TreeNode(1, "Система керування клінікою")

    # Додаємо фактори (F1, F2, F3)
    F1 = TreeNode(2, "F1: Управління даними пацієнтів")
    F2 = TreeNode(3, "F2: Управління записами на прийом")
    F3 = TreeNode(4, "F3: Управління платежами")

    root.add_child(F1)
    root.add_child(F2)
    root.add_child(F3)

    # Додаємо критерії до F1
    K1 = TreeNode(5, "K1: Безпека даних")
    K2 = TreeNode(6, "K2: Зручність доступу")
    F1.add_child(K1)
    F1.add_child(K2)

    # Додаємо критерії до F2
    K3 = TreeNode(7, "K3: Швидкість запису")
    K4 = TreeNode(8, "K4: Зручність інтерфейсу")
    F2.add_child(K3)
    F2.add_child(K4)

    # Додаємо критерії до F3
    K5 = TreeNode(9, "K5: Точність розрахунків")
    F3.add_child(K5)

    return root


# Приклад використання програми
if __name__ == "__main__":
    clinic_hierarchy = build_clinic_hierarchy()
    clinic_hierarchy.print_tree()