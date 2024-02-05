from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup_requires = []

install_requires = [
    'pygame==2.5.2',
]

dependency_links = []


setup(
    name='codes-with-pygame',
    version=open('VERSION').read().strip(),
    url='https://https://github.com/rohawolf/codes-with-pygame',
    description='',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    author='Roha Park',
    author_email='rohawolf@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    scripts=['manage.py'],
    entry_points={
        'console_scripts': [

        ]
    },
    zip_safe=False,
    python_requires=f">={open('.python-version').read().strip()}",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
    ],
)
