#include <stdio.h>
#include <wchar.h>
#include <locale.h>

#define FIND_MAX(a, b) ((a) > (b) ? (a) : (b))

#define GET_INPUT(prompt, var) \
do { \
        wprintf(L"%ls", prompt); \
        wscanf(L"%d", &var); \
        while(getwchar() != L'\n');  \
} while (0)

int main() {
    setlocale(LC_ALL, "");
    int n, max = 0;

    GET_INPUT(L"Введите количество чисел: ", n);

    for (int i = 0; i < n; ++i) {
        int num;
        GET_INPUT(L"Введите число: ", num);
        max = FIND_MAX(max, num);
    }

    wprintf(L"Максимальное число: %d\n", max);

    return 0;
}
