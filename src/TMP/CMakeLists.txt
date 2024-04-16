cmake_minimum_required(VERSION 3.8)
project(TMP)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})

# Install URDF files
install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME})

# Install mesh files
install(DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME})

# Install world files
install(DIRECTORY worlds
  DESTINATION share/${PROJECT_NAME})

# Install parameter files
install(DIRECTORY param
  DESTINATION share/${PROJECT_NAME})

# Install script files
install(DIRECTORY script
  DESTINATION share/${PROJECT_NAME})

ament_package()

