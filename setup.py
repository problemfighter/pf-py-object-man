from setuptools import setup, find_packages

setup(
    name='pf-py-object-man',
    version='1.0',
    url='https://github.com/problemfighter/pf-py-object-man',
    license='Apache 2.0',
    author='Touhid Mia',
    author_email='hmtm.cse@gmail.com',
    description='Problem Fighter Python Object Manager',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)