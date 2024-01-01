#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
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
   
    view_gzbwrd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'view_gzbwrd.launch.py')]),
    )
    
    # Gazeboda bir varlık oluşturmak için spawn_entity düğümünü başlatiyoruz
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
        '-topic', 'robot_description',
        '-entity', 'my_bot',
        '-x', '0',
        '-y', '2',
        '-z', '0'],
        output='screen'
    )

    return LaunchDescription([
        # Oluşturulan parçaları başlatmak için başka başlatma betiklerini içeri aktarın
        rsp,
        view_gzbwrd,
        spawn_entity,
    ])
