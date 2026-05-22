cmake_minimum_required(VERSION 3.15)
project(onx)

file(REMOVE ${CMAKE_CURRENT_SOURCE_DIR}/bar.cpp)

find_package(Python REQUIRED)

if(Python_EXECUTABLE)
  execute_process(
    COMMAND ${Python_EXECUTABLE} "onx.py"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    RESULT_VARIABLE ONX_RESULT)
  if(NOT ONX_RESULT EQUAL "0")
    message(FATAL_ERROR "onx.py failed with ${ONX_RESULT}")
  endif()
endif()

add_executable(onx bar.cpp)
