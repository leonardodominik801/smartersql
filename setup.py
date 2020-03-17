import sys
from setuptools import setup, find_packages

setup(
    name = "smartersql",
    version = "0.1",
    description = "A smarter interface to SQL.",
    author = "Aaron Swartz",
    author_email = "me@aaronsw.com",
    url='https://github.com/aaronsw/watchdog/blob/master/vendor/smartersql.py',
    classifiers=[],
    license='AGPLv3',
    packages=find_packages(),
    py_modules=['smartersql'],
    include_package_data=True,
    zip_safe=False
)