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
            os.path.join(get_package_share_directory('ms_robot'), 'launch/rviz2_launch.py')
        )
    )

    # Harita servisi launch açıklaması
    mapser_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ms_robot'), 'launch/my_map_launch.py')
        )
    )

    # Genel simülasyon launch açıklaması
    sim_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ms_robot'), 'launch/sim_launch.py')
        )
    )

    # AMCL launch açıklaması
    amcl_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ms_robot'), 'launch/amcl_launch.py')
        )
    )

    # Navigasyon launch açıklaması
    navig_l = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ms_robot'), 'launch/navigation_launch.py')
        )
    )

    # Aksiyonları sırayla ekleyerek LaunchDescription nesnesini oluştur
    ld.add_action(navig_l)   
    ld.add_action(amcl_l)
    ld.add_action(sim_l)
    ld.add_action(mapser_l)
    ld.add_action(rviz_l) 

    return ld
