from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0',    
    description='A example Python package',
    url='https://github.com/yasirrivu/DSSS_HOMEWORK_2/tree/main',
    author='Yasir Al Hasan ',
    license='Apache License',
    packages=['math_quiz'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache License 2.0',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
