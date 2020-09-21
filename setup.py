import setuptools

setuptools.setup(
    name='Pawn',
    version='1.0.0',
    author='QLabs',
    description='A Simple, Lightweight, Python Chess Graphics Package',
    long_description=open("README.md","r").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/quantalabs/pawn",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment :: Board Games',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.8',
    project_urls={
        'Bug Reports': 'https://github.com/quantalabs/pawn/issues',
        'Source': 'https://github.com/quantalabs/pawn',
    },
)