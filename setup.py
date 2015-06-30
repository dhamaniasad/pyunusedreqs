from setuptools import setup

install_requires = [
    # 'requests',
    # 'beautifulsoup4'
]

setup(
    name='pyunusedreqs',
    install_requires=install_requires,
    version=0.1,
    description='Finds unused libraries in a requirements.txt file given a Python project',
    author='Asad Dhamani',
    author_email='dhamaniasad+code@gmail.com',
    url='https://github.com/dhamaniasad/pyunusedreqs',
    license='Unlicense',
    py_modules=['pyunusedreqs'],
    entry_points={
        'console_scripts': [
            'unusedreqs = pyunusedreqs:command_line_runner'
        ]
    }
)
