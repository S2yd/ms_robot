#!/usr/bin/env python3

import os
import launch

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    #hospital
    #hospital_three_floors
    #hospital_two_floors
    #obstacles
    world_file_name = "hospital.world"
    world = os.path.join(get_package_share_directory('ms_robot'), 'worlds', world_file_name)
    gazebo_ros = get_package_share_directory('gazebo_ros')

    gazebo_client = launch.actions.IncludeLaunchDescription(
	launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros, 'launch', 'gzclient.launch.py')),
        condition=launch.conditions.IfCondition(launch.substitutions.LaunchConfiguration('gui'))
     )
    gazebo_server = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros, 'launch', 'gzserver.launch.py'))
    )

    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
          'world',
          default_value=[world, ''],
          description='SDF world file'),
        launch.actions.DeclareLaunchArgument(
            name='gui',
            default_value='false'
        ),
        gazebo_server,
        gazebo_client
    ])
    return ld

