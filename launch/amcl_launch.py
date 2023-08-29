#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # AMCL düğümü konfigürasyonu
    amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        output='screen',
        parameters=["/home/mohammed/ros2_ws/src/articubot_one/config/amcl_file.yaml"]
    )
    
    # Yaşam döngüsü yöneticisi için gerekli parametreler
    lifecycle_nodes = ['amcl']
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
        amcl,
        start_lifecycle_manager_cmd,
    ])
