
"""
JUJU
--------------
REST application framework with expressive, elegant structure.
"""
from setuptools import setup



setup(
    name='JUJU-CLI',
    version='0.6',
    url='http://github.com/laith43d/juju/',
    license='MIT',
    author='Layth Zahid',
    author_email='L@LZAH.online',
    description=('REST application framework with expressive, elegant structure.'),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite="tests",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)