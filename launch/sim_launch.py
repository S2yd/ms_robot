#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Kullanılacak paket adı
    package_name = 'ms_robot'

    # Robot Durum Yayıncısı'nın başlatılması için başka bir başlatma betiğini içeri aktarın
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'rsp.launch.py')]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Gazebo dünyasını belirlemek için argümanı tanımlayın
    world_arg = DeclareLaunchArgument(
        'world',
        default_value=[os.path.join(get_package_share_directory('ms_robot'), 'worlds', 'obstacles.world')],
        description='world:=./src/ms_robot/worlds/obstacles.world'
    )

    # Gazebo'nun başlatılması için başka bir başlatma betiğini içeri aktarın
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    )

    # Gazebo'da bir varlık oluşturmak için spawn_entity düğümünü başlatın
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description',
                   '-entity', 'my_bot'],
        output='screen'
    )

    return LaunchDescription([
        # Oluşturulan parçaları başlatmak için başka başlatma betiklerini içeri aktarın
        rsp,
        world_arg,
        gazebo,
        spawn_entity,
    ])
