from setuptools import find_packages, setup

package_name = 'my_py_first'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='phyw',
    maintainer_email='phyw@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "my_first_py = my_py_first.my_first_py:main",
            "py_sub = my_py_first.py_subscriber:main",
            "py_pub = my_py_first.py_publisher:main",
            "number_pub = my_py_first.number_pub:main", 
            "number_counter = my_py_first.number_counter:main", 
            "adder_service = my_py_first.add_service:main", 
            "adder_client = my_py_first.add_client:main", 
            "hardware_pub = my_py_first.hardware_status_pub:main",
            "hardware_sub = my_py_first.hardware_status_sub:main",

        ],
    },
)
