import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    package_name='articubot_one' 

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    world_arg = DeclareLaunchArgument(
        'world',
        default_value=[os.path.join(get_package_share_directory('articubot_one'), 'worlds', 'obstacles.world')],
        description='world:=./src/articubot_one/worlds/obstacles.world'
    )
   
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen'
    )

    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[{'use_sim_time': True}],
    )
    
    """
    navigation_node = Node(
        package='nav2_bringup',
        executable='bringup',
        name='navigation',
        output='screen',
        parameters=[{'use_sim_time': True}],
    )
    """
    return LaunchDescription([
        rsp,
        world_arg,
        gazebo,
        spawn_entity,
        slam_node,
       #navigation_node,
    ])
