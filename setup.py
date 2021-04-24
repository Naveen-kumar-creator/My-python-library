from setuptools import find_packages, setup
setup(
    name='Copy Method',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='My first Python library',
    author='Anonymous',
    license='MIT',
    install_requires=['pyrogram==1.2.9'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
