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

    # Додавання дочірнього елемента
    def add_child(self, child):
        child.parent = self
        child.level = self.level + 1

        if self.first_child is None:
            self.first_child = child
        else:
            sibling = self.first_child
            while sibling.next:
                sibling = sibling.next
            sibling.next = child
            child.prev = sibling

        self.count_next_level += 1

    # Рекурсивний вивід дерева
    def print_tree(self, indent=0):
        print("  " * indent + f"{self.name} (Рівень: {self.level})")
        
        child = self.first_child
        while child:
            child.print_tree(indent + 1)
            child = child.next
