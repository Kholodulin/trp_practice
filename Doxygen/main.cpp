// main.cpp
#include <iostream>
#include <Eigen/Dense>

/**
 * @brief Главная функция программы.
 *
 * В данной программе создаются матрицы, выполняются операции
 * транспонирования и умножения, и выводится результат.
 *
 * @return Код возврата программы.
 */
int main() {
    /**
     * @brief Создание матриц.
     */
    Eigen::MatrixXd matrix1(3, 2);
    Eigen::MatrixXd matrix2(3, 2);

    /**
     * @brief Заполнение матриц значениями.
     */
    matrix1 << 1, 2,
        3, 4,
        5, 1;

    matrix2 << 3, 1,
        2, 7,
        2, 4;

    /**
     * @brief Транспонирование матрицы.
     */
    Eigen::MatrixXd transposedMatrix2 = matrix2.transpose();

    /**
     * @brief Умножение матриц.
     */
    Eigen::MatrixXd result = matrix1 * transposedMatrix2;

    /**
     * @brief Вывод результата.
     */
    std::cout << "matrix1 * matrix2.transpose():\n"
              << result << std::endl;

    /**
     * @brief Ожидание ввода пользователя перед завершением программы.
     */
    system("pause");

    /**
     * @brief Код возврата программы.
     */
    return 0;
}
