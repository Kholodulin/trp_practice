#include <iostream>
#include <CL/cl.h>

int main() {
    const int n = 10;
    int array1[n];
    int array2[n];
    int result[n];

    for (int i = 0; i < n; ++i) {
        array1[i] = i;
        array2[i] = i * 2;
    }

    cl_platform_id platform;
    clGetPlatformIDs(1, &platform, nullptr);

    cl_device_id device;
    clGetDeviceIDs(platform, CL_DEVICE_TYPE_GPU, 1, &device, nullptr);

    cl_context context = clCreateContext(nullptr, 1, &device, nullptr, nullptr, nullptr);
    cl_command_queue queue = clCreateCommandQueue(context, device, 0, nullptr);

    // Создание буферов для массивов на устройстве
    cl_mem buffer1 = clCreateBuffer(context, CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR, sizeof(int) * n, array1, nullptr);
    cl_mem buffer2 = clCreateBuffer(context, CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR, sizeof(int) * n, array2, nullptr);
    cl_mem bufferResult = clCreateBuffer(context, CL_MEM_WRITE_ONLY, sizeof(int) * n, nullptr, nullptr);

    // Загрузка программы OpenCL из исходного кода
    const char* source_code = R"(
        __kernel void add_arrays(__global const int* array1, __global const int* array2, __global int* result) {
            int gid = get_global_id(0);
            result[gid] = array1[gid] + array2[gid];
        }
    )";

    cl_program program = clCreateProgramWithSource(context, 1, &source_code, nullptr, nullptr);
    clBuildProgram(program, 1, &device, nullptr, nullptr, nullptr);
    cl_kernel kernel = clCreateKernel(program, "add_arrays", nullptr);

    // Установка аргументов ядра
    clSetKernelArg(kernel, 0, sizeof(cl_mem), &buffer1);
    clSetKernelArg(kernel, 1, sizeof(cl_mem), &buffer2);
    clSetKernelArg(kernel, 2, sizeof(cl_mem), &bufferResult);

    // Запуск ядра
    size_t global_size = n;
    clEnqueueNDRangeKernel(queue, kernel, 1, nullptr, &global_size, nullptr, 0, nullptr, nullptr);
    clFinish(queue);

    // Чтение данных из буфера результата обратно в массив
    clEnqueueReadBuffer(queue, bufferResult, CL_TRUE, 0, sizeof(int) * n, result, 0, nullptr, nullptr);

    std::cout << "mass 1: ";
    for (int i = 0; i < n; ++i) {
        std::cout << array1[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "mass 2: ";
    for (int i = 0; i < n; ++i) {
        std::cout << array2[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "result: ";
    for (int i = 0; i < n; ++i) {
        std::cout << result[i] << " ";
    }
    std::cout << std::endl;

    // Очистка ресурсов
    clReleaseMemObject(buffer1);
    clReleaseMemObject(buffer2);
    clReleaseMemObject(bufferResult);
    clReleaseKernel(kernel);
    clReleaseProgram(program);
    clReleaseCommandQueue(queue);
    clReleaseContext(context);
    system("pause");
    return 0;
}
