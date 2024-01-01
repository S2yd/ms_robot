#!/usr/bin/env python3

import launch
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                [get_package_share_directory('ms_robot'), '/launch/gzbwrd.launch.py']
            ),
            launch_arguments={
                'gui': 'true'
            }.items()
        )
    ])
    return ld

