from setuptools import setup

package_name = 'rmf_test_ci'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    author='youliang',
    author_email='youaliign@openrobotics.org',
    zip_safe=True,
    maintainer='youaliign',
    maintainer_email='youaliign@openrobotics.org',
    description='A package containing scripts for demos',
    license='Apache License Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'test_script = rmf_test_ci.test_script:main'
        ],
    },
)
