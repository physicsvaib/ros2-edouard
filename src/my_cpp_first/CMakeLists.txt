 cmake_minimum_required(VERSION 3.8)
project(my_cpp_first)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(cpp_first_node src/my_first_cpp.cpp)
ament_target_dependencies(cpp_first_node rclcpp)

install(TARGETS 
  cpp_first_node 
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
