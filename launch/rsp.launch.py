import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():

    # Lance parametreleri
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_ros2_control = LaunchConfiguration('use_ros2_control')

    # Robot tanımını alınacak Xacro dosyasının yolu
    pkg_path = os.path.join(get_package_share_directory('ms_robot'))
    xacro_file = os.path.join(pkg_path, 'description', 'robot.urdf.xacro')

    # Robot tanımı için komut oluşturun
    robot_description_config = Command(['xacro ', xacro_file, ' use_ros2_control:=', use_ros2_control, ' sim_mode:=', use_sim_time])
    
    # Parametreler
    params = {'robot_description': robot_description_config, 'use_sim_time': use_sim_time}

    # Robot durum yayıncısı düğümünü oluşturun
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    return LaunchDescription([
        # Lance argümanlarını tanımlayın
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Eğer true ise sim zamanı kullan'),
        DeclareLaunchArgument(
            'use_ros2_control',
            default_value='true',
            description='Eğer true ise ros2_control kullan'),

        # Robot durum yayıncısı düğümünü ekleyin
        node_robot_state_publisher
    ])
