from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    # RViz launch açıklaması
    rviz_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('articubot_one'), 'launch/rviz2_launch.py')
        )
    )

    # Harita servisi launch açıklaması
    mapser_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('articubot_one'), 'launch/my_map_launch.py')
        )
    )

    # Genel simülasyon launch açıklaması
    allaun_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('articubot_one'), 'launch/sim_launch.py')
        )
    )

    # AMCL launch açıklaması
    amcl_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('articubot_one'), 'launch/amcl_launch.py')
        )
    )

    # Navigasyon launch açıklaması
    navig_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('articubot_one'), 'launch/navigation_launch.py')
        )
    )

    # Aksiyonları sırayla ekleyerek LaunchDescription nesnesini oluştur
    ld.add_action(navig_l)   
    ld.add_action(amcl_l)
    ld.add_action(allaun_l)
    ld.add_action(mapser_l)
    ld.add_action(rviz_l) 

    return ld
