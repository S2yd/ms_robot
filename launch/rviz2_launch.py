from launch import LaunchDescription
from launch.actions import  ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['rviz2' ],
            # ,'--display-config=default'
            output='screen'
        )
    ])