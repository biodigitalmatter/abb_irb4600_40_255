import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import AnyLaunchDescriptionSource
from launch_testing.actions import ReadyToTest
import pytest


# Executes the given launch file and checks if all nodes can be started
@pytest.mark.rostest
def generate_test_description():
    launch_include = IncludeLaunchDescription(
        AnyLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('abb_irb4600_40_255'),
                'launch/description.launch.xml',
            )
        ),
    )

    return LaunchDescription([launch_include, ReadyToTest()])


# Executes the given launch file and checks if all nodes can be started
@pytest.mark.rostest
def generate_test_display():
    launch_include = IncludeLaunchDescription(
        AnyLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('abb_irb4600_40_255'),
                'launch/display.launch.xml',
            )
        ),
    )

    return LaunchDescription([launch_include, ReadyToTest()])
