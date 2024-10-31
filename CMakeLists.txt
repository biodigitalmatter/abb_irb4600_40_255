cmake_minimum_required(VERSION 3.8)
project(abb_irb4600_40_255)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch meshes rviz test urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
    ament_add_pytest_test(launch_files test/test_launch_files.py)

  find_package(ament_lint_auto REQUIRED)
  list(APPEND AMENT_LINT_AUTO_EXCLUDE
      ament_cmake_copyright
  )
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
