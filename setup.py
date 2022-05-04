from setuptools import setup
from setuptools import find_packages


def setup_package():

    with open("README.md", "r") as fh:
        long_description = fh.read()

    from xcomplex import __version__
    REQUIRES = ['numpy']
    META_DATA = dict(
        name='xcomplex',
        version=__version__,
        description='Subject assignment tool',
        author='Nicolas Cardiel',
        author_email='cardiel@ucm.es',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages('.'),
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        install_requires=REQUIRES,
        zip_safe=False
        )

    setup(**META_DATA)


if __name__ == '__main__':
    setup_package()
