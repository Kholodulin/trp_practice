cmake_minimum_required(VERSION 3.14)

project(cl LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core)

set(CMAKE_PREFIX_PATH "C:/vcpkg/installed/x64-windows")
find_package(OpenCL REQUIRED)

add_executable(cl
  main.cpp
)
target_link_libraries(cl Qt${QT_VERSION_MAJOR}::Core OpenCL::OpenCL)

include(GNUInstallDirs)
install(TARGETS cl
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
