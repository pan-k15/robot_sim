from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():

    return LaunchDescription([

        ExecuteProcess(
            cmd=[
                'gz', 'sim',
                '-r',                     # run immediately
                '/home/pan/Documents/projects/robot/p3/ros2_ws/src/robot_simulation/worlds/test.sdf'
            ],
            output='screen'
        ),

    ])
