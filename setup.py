from setuptools import setup, find_packages

setup(
    name='seav',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy'
    ],
    url='https://github.com/seav3r/seav',
    author='Christopher Bernard',
    author_email='christopher.s.bernard@gmail.com',
    description='A place to place my personal scripts',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
    ]
)
