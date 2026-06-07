from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'game_one'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lenovoi',
    maintainer_email='bhagabantagiri@gmail.com',
    description='A beginner-level ROS2 micro-project demonstrating node sommunication and basic control loops using Turtlesim',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'game_one = game_one.game_one:main'
        ],
    },
)
