import numpy as np
import pandas as pd  # Для табличного виведення матриць


class PairwiseComparisonMatrix:
    def __init__(self, elements):
        self.elements = elements
        self.size = len(elements)
        self.matrix = np.ones((self.size, self.size))  # Ініціалізація матриці одиницями

    def input_comparisons(self):
        print("\nВведіть оцінки парних порівнянь:")
        for i in range(self.size):
            for j in range(i + 1, self.size):
                while True:
                    try:
                        score = float(input(
                            f"Оцінка для {self.elements[i]} відносно {self.elements[j]} (приклад: 3, 0.5): "
                        ))
                        self.matrix[i, j] = score
                        self.matrix[j, i] = 1 / score
                        break
                    except ValueError:
                        print("Помилка введення! Будь ласка, введіть числове значення у форматі: 3 або 0.5.")

        print("\nЗаповнена матриця парних порівнянь:")
        self.display_matrix()

    def calculate_priorities_and_lambda(self):
        column_sums = np.sum(self.matrix, axis=0)
        normalized_matrix = self.matrix / column_sums
        priorities = np.mean(normalized_matrix, axis=1)

        # Обчислення λ_max
        weighted_sum = np.dot(self.matrix, priorities)
        lambda_max = np.mean(weighted_sum / priorities)

        return priorities, lambda_max

    def display_matrix(self):
        df = pd.DataFrame(self.matrix, index=self.elements, columns=self.elements)
        print(df)


def matrix_multiplication(weights, priorities):
    """
    Виконує множення матриці ваг на вектори пріоритетів.
    """
    result = np.dot(weights, priorities)
    return result


def main():
    print("Стоматологічна клініка: Аналіз альтернатив для вибору IT-рішень")

    # Фактори та критерії
    factors = ["F1: Ефективність", "F2: Зручність використання"]
    criteria_by_factor = {
        "F1": ["K1: Облік медичної інформації", "K2: Доступ до історії лікувань", "K3: Планування візитів"],
        "F2": ["K4: Облік платежів", "K5: Генерація фінансових звітів", "K6: Планування бюджету"]
    }

    # Альтернативи
    alternatives = ["A1: Microsoft Access", "A2: MySQL", "A3: Хмарна платформа", "A4: Спеціалізоване ПЗ"]

    # Заповнення матриці факторів
    print("\nЗаповнення матриці парних порівнянь для факторів:")
    factor_matrix = PairwiseComparisonMatrix(factors)
    factor_matrix.input_comparisons()
    factor_priorities, _ = factor_matrix.calculate_priorities_and_lambda()
    print("\nВектор пріоритетів факторів:")
    for i, priority in enumerate(factor_priorities):
        print(f"{factors[i]}: {priority:.3f}")

    # Заповнення матриць критеріїв для кожного фактора
    criteria_weights_by_factor = {}
    for factor, criteria in criteria_by_factor.items():
        print(f"\nЗаповнення матриці для критеріїв, пов'язаних із фактором {factor}:")
        criteria_matrix = PairwiseComparisonMatrix(criteria)
        criteria_matrix.input_comparisons()
        criteria_priorities, _ = criteria_matrix.calculate_priorities_and_lambda()
        criteria_weights_by_factor[factor] = criteria_priorities
        print(f"\nВектор пріоритетів для критеріїв ({factor}):")
        for i, priority in enumerate(criteria_priorities):
            print(f"{criteria[i]}: {priority:.3f}")

    # Заповнення матриць альтернатив для кожного критерію
    alternative_priorities_by_criterion = {}
    for factor, criteria in criteria_by_factor.items():
        for criterion in criteria:
            print(f"\nЗаповнення матриці для альтернатив за критерієм {criterion}:")
            alternative_matrix = PairwiseComparisonMatrix(alternatives)
            alternative_matrix.input_comparisons()
            priorities, _ = alternative_matrix.calculate_priorities_and_lambda()
            alternative_priorities_by_criterion[criterion] = priorities
            print(f"\nВектор пріоритетів для альтернатив ({criterion}):")
            for i, priority in enumerate(priorities):
                print(f"{alternatives[i]}: {priority:.3f}")

    # Обчислення векторів пріоритетів альтернатив відносно факторів
    alternative_priorities_by_factor = {}
    for factor, criteria in criteria_by_factor.items():
        criteria_weights = criteria_weights_by_factor[factor]
        priorities_matrix = np.array([alternative_priorities_by_criterion[criterion] for criterion in criteria])
        alternative_priorities = matrix_multiplication(criteria_weights, priorities_matrix)
        alternative_priorities_by_factor[factor] = alternative_priorities

        print(f"\nВектор пріоритетів альтернатив відносно {factor}:")
        for i, priority in enumerate(alternative_priorities):
            print(f"{alternatives[i]}: {priority:.3f}")

    # Обчислення остаточного вектора пріоритетів для фокусу ієрархії
    final_priorities = matrix_multiplication(factor_priorities, np.array(list(alternative_priorities_by_factor.values())))
    print("\nОстаточний вектор пріоритетів для фокусу ієрархії:")
    for i, priority in enumerate(final_priorities):
        print(f"{alternatives[i]}: {priority:.3f}")
    
    # Знаходження альтернативи з найбільшим пріоритетом
    max_index = np.argmax(final_priorities)  # Індекс максимальної пріоритетної альтернативи
    print(f"{alternatives[max_index]} з пріоритетом {final_priorities[max_index]:.3f}")

if __name__ == "__main__":
    main()
