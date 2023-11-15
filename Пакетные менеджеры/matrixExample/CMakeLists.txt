cmake_minimum_required(VERSION 3.14)

project(matrixExample LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core)

set(CMAKE_PREFIX_PATH "C:/vcpkg/installed/x64-windows")
find_package(Eigen3 CONFIG REQUIRED)

add_executable(matrixExample
  main.cpp
)

target_link_libraries(matrixExample PRIVATE Qt${QT_VERSION_MAJOR}::Core Eigen3::Eigen)

include(GNUInstallDirs)
install(TARGETS matrixExample
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

