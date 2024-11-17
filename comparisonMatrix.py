import numpy as np

class PairwiseComparisonMatrix:
    def __init__(self, criteria):
        self.criteria = criteria
        self.size = len(criteria)
        self.matrix = np.ones((self.size, self.size))
    
    def input_comparisons(self):
        print("Введіть оцінки парних порівнянь для критеріїв:")
        for i in range(self.size):
            for j in range(i + 1, self.size):
                score = float(input(f"Оцінка для {self.criteria[i]} відносно {self.criteria[j]} (приклад: 3, 0.5): "))
                self.matrix[i, j] = score
                self.matrix[j, i] = 1 / score
    
    def calculate_priorities(self):
        column_sums = np.sum(self.matrix, axis=0)
        normalized_matrix = self.matrix / column_sums
        priorities = np.mean(normalized_matrix, axis=1)
        return priorities
    
    def calculate_lambda_max(self, priorities):
        weighted_sum = np.dot(self.matrix, priorities)
        lambda_max = np.sum(weighted_sum / priorities) / self.size
        return lambda_max

    def calculate_principal_eigenvalue_and_vector(self):
        # Знаходимо власні значення та власні вектори матриці
        eigenvalues, eigenvectors = np.linalg.eig(self.matrix)
        
        # Вибираємо найбільше власне значення та відповідний власний вектор
        max_index = np.argmax(eigenvalues)
        principal_eigenvector = eigenvectors[:, max_index].real  # тільки дійсна частина
        
        return principal_eigenvector

    def display_matrix(self):
        print("\nМатриця парних порівнянь:")
        for row in self.matrix:
            print(["{:.2f}".format(x) for x in row])

def matrix_multiplication(matrix_a, matrix_b):
    """ Функція для множення двох матриць """
    # Перевірка розмірності
    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці")
    
    # Множення матриць
    result = np.dot(matrix_a, matrix_b)
    return result

# Приклад матриць для множення
# Матриця критеріїв для факторів
criteria_matrix = np.array([
    [1, 2, 0.5],
    [0.5, 1, 3],
    [2, 0.333, 1]
])

# Матриця альтернатив щодо одного з критеріїв (наприклад, "Доступ до даних")
alternatives_matrix = np.array([
    [1, 4, 0.5],
    [0.25, 1, 3],
    [2, 0.333, 1]
])

# Множення матриць критеріїв та альтернатив
result_matrix = matrix_multiplication(criteria_matrix, alternatives_matrix)

# Критерії для стоматологічної клініки
criteria = ["Доступ до даних", "Зручність інтерфейсу", "Інтеграція з програмами", "Адекватність функціоналу"]

# Створення об'єкта для матриці порівнянь
comparison_matrix = PairwiseComparisonMatrix(criteria)

# Введення даних експертного опитування
comparison_matrix.input_comparisons()

# Виведення матриці парних порівнянь
comparison_matrix.display_matrix()

# Обчислення пріоритетів
priorities = comparison_matrix.calculate_priorities()

print("\nВектор пріоритетів:")
for i, priority in enumerate(priorities):
    print(f"{criteria[i]}: {priority:.3f}")

# Обчислення λmax
lambda_max = comparison_matrix.calculate_lambda_max(priorities)
print(f"\nНайбільше власне значення λmax: {lambda_max:.3f}")

# Обчислення головного власного значення та вектора
eigenvector = comparison_matrix.calculate_principal_eigenvalue_and_vector()

print("\nВласний вектор, що відповідає λmax:")
for i, value in enumerate(eigenvector):
    print(f"{criteria[i]}: {value:.3f}")

# Виведення результату множення матриць
print("Результат множення матриць:")
print(result_matrix)