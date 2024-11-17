class TreeNode:
    def __init__(self, number, name, level=0, parent=None):
        self.number = number               # Номер елемента дерева
        self.name = name                   # Назва елемента дерева
        self.level = level                 # Номер рівня ієрархії
        self.parent = parent               # Вказівник на елемент-предка
        self.prev = None                   # Вказівник на попередній елемент того ж рівня
        self.next = None                   # Вказівник на наступний елемент того ж рівня
        self.first_child = None            # Вказівник на перший елемент наступного рівня
        self.count_next_level = 0          # Кількість елементів наступного рівня
        self.matr = None                   # Матриця парних порівнянь (якщо є)
        self.w = None                      # Вектор пріоритетів (якщо є)

    def add_child(self, child):
        """Додає дочірній вузол."""
        child.parent = self
        child.level = self.level + 1
        if not self.first_child:
            self.first_child = child
        else:
            current = self.first_child
            while current.next:
                current = current.next
            current.next = child
            child.prev = current
        self.count_next_level += 1

    def print_tree(self):
        """Виводить дерево у консоль."""
        indent = "  " * self.level
        print(f"{indent}{self.number}: {self.name}")
        child = self.first_child
        while child:
            child.print_tree()
            child = child.next

    def navigate(self, target_number):
        """Рекурсивний пошук вузла за номером."""
        if self.number == target_number:
            return self

        child = self.first_child
        while child:
            result = child.navigate(target_number)
            if result:
                return result
            child = child.next

        return None