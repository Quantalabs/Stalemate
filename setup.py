import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Pawn',
    version='1.0.0',
    author='QLabs',
    description='A Simple, Lightweight, Python Chess Graphics Package',
    long_description=long_description,
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