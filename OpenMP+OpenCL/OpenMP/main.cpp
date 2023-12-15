#include <iostream>
#include <omp.h>


int main() {
    const int size = 100;
    int array[size];
    int sum = 0;

    for (int i = 0; i < size; ++i) {
        array[i] = i + 1;
    }

    // Параллельное вычисление суммы с использованием OpenMP
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < size; ++i) {
        sum += array[i];
    }

    std::cout << "result: " << sum << std::endl;
    system("pause");

    return 0;
}

