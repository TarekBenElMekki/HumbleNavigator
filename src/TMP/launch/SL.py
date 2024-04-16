import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get the share directory of the 'TMP' package
    pkg_share = get_package_share_directory('TMP')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([pkg_share, '/launch/gazebo.launch.py'])
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([pkg_share, '/launch/rviz.launch.py'])
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([pkg_share, '/launch/navigation.launch.py'])
        )
    ])

