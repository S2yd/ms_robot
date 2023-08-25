from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'ms_save': '/home/mohammed/ros2_ws/ms_save'}] 
        )
    ])
