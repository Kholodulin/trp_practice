#include <iostream>
#include <Eigen/Dense>

int main() {
    Eigen::MatrixXd matrix1(3, 2);
    Eigen::MatrixXd matrix2(3, 2);

    matrix1 << 1, 2,
               3, 4,
               5, 1;

    matrix2 << 3, 1,
               2, 7,
               2, 4;
    //транспонирование матрицы 2
    Eigen::MatrixXd transposedMatrix2 = matrix2.transpose();
    //умножение матриц
    Eigen::MatrixXd result = matrix1 * transposedMatrix2;

    std::cout << "matrix1 * matrix2.transpose():\n"
              << result << std::endl;

    system("pause");
    return 0;
}
