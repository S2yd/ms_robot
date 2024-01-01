#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # Harita dosyasının yolu
    map_path = os.path.join(get_package_share_directory('ms_robot'), 'config', 'hospital_map_save.yaml' )

    # Harita sunucusu düğümü
    map_server_cmd = Node(
        package='nav2_map_server',
        executable='map_server',
        output='screen',
        parameters=[{'yaml_filename': map_path,
                    'use_sim_time': True}]
    )

    # Yaşam döngüsü yöneticisi düğümü için gerekli parametreler
    lifecycle_nodes = ['map_server']
    autostart = True

    # Yaşam döngüsü yöneticisi düğümünü başlatma komutu
    start_lifecycle_manager_cmd = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_localization',
        output='screen',
        emulate_tty=True,
        parameters=[{'use_sim_time': True},
                    {'autostart': autostart},
                    {'node_names': lifecycle_nodes}])

    # Başlatma açıklamalarını içeren bir liste döndürme
    return LaunchDescription([
        map_server_cmd,
        start_lifecycle_manager_cmd,
    ])
