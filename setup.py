from setuptools import setup, find_packages
setup(
    name = 'task_manager',
    version= '0.1.0',
    description='GUI app to manager your daily task',
    author='Canrong Qiu (Jackey)',
    author_email='canrong.qiu@desy.de',
    url='https://github.com/jackey-qiu/pyTask',
    classifiers=['Topic :: pyQt application',
                 'Programming Language :: Python'],
    license='MIT',
    install_requires=['PyQt5','pyqtgraph','qdarkstyle','pandas'],
    packages=find_packages(),
    # packages=find_packages(where='library_manager'),
    # package_dir={'': 'library_lanager'},
    package_data={'task_manager.resources':['task_files/*','ui/*.*']},
    scripts=['./task_manager/bin/task_manager_gui.py'],
    entry_points = {
        'console_scripts' : [
            'task = task_manager.bin.task_manager_gui:main'
        ],
    }
)