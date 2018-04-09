from setuptools import setup, find_packages
 
setup(name='onem2m',
    version='0.1',
    url='https://github.com/kimkeehwan/onem2m_adn_lib_python',
    license='MIT',
    author='Kim keehwan',
    author_email='kimkeehwan@handysoft.co.kr',
    description='oneM2M ADN Client Lib',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3.5'
    ],
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    zip_safe=False,
    setup_requires=['configparser>=3.5.0', 'requests>=2.18.4'])