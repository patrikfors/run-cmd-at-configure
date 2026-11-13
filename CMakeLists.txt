cmake_minimum_required(VERSION 3.15)
project(onx CXX)

find_package(Python REQUIRED COMPONENTS Interpreter)

if(NOT Python_EXECUTABLE)
  message(FATAL_ERROR "This won't do, python interpreter not found")
endif()

#-- Run onx.py at configure time to generate bar.cpp
execute_process(
  COMMAND ${Python_EXECUTABLE} "onx.py" "${CMAKE_CURRENT_BINARY_DIR}/bar.cpp"
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  RESULT_VARIABLE ONX_RESULT)
if(NOT ONX_RESULT EQUAL "0")
  message(FATAL_ERROR "onx.py failed with ${ONX_RESULT}")
endif()

#-- Run onx.py at build time to generate baz.cpp
# The script runs when bar.cpp is missing or its dependencies
# change, not on every build. For a command that should run
# every build, use add_custom_target(... ALL COMMAND ...) instead.
add_custom_command(
  OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/baz.cpp"
  COMMAND "${Python_EXECUTABLE}" "${CMAKE_CURRENT_SOURCE_DIR}/onx.py" "${CMAKE_CURRENT_BINARY_DIR}/baz.cpp" "build_phase"
  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  USES_TERMINAL  # or my fancy animation won't show
  DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/onx.py"
          "${CMAKE_CURRENT_SOURCE_DIR}/foo.cpp.in"
  VERBATIM
)

add_executable(onx ${CMAKE_CURRENT_BINARY_DIR}/bar.cpp)
add_executable(onx2 EXCLUDE_FROM_ALL ${CMAKE_CURRENT_BINARY_DIR}/baz.cpp)
