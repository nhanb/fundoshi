import os
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='fundoshi',
    version='0.0.4',
    description='Get manga series & chapter data from various reader sites.',
    long_description=read('README.rst'),
    url='http://github.com/nhanb/fundoshi',
    license='MIT',
    author='Bùi Thành Nhân',
    author_email='nhan@nerdyweekly.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=['beautifulsoup4', 'requests', 'cfscrape'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
