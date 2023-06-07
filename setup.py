"""
group_project_personal_helper

This module provides the setup configuration for the Group Project Personal Helper bot.
The bot collects information entered by clients and stores it in the directory. 
It can also display it on the screen if necessary.
"""
from setuptools import setup
setup(
    name='group_project_personal_helper',
    version='0.1',
    data_files=[('', ['README.md'])],
    description='the bot collects information entered by clients and stores it in the directory, it can also display it on the screen if necessary',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
    authors=['Oleksandr Revuka', 'Oleksandr Shevchenko', 'Evgen Kulik',
             'Roman Lomachinskiy', 'Oleksii Chaika', 'Artem Ivanina'],
    license='MIT',
    python_requires='>=3.11',
    entry_points={'console_scripts': ['pbot = personal_helper.run_bot:main']}    
)
