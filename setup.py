"""
avwx package metadata
"""

from setuptools import setup

# Temp fix for not-yet-installed lib error on fresh install
__author__ = "Michael duPont"
__maintainer__ = "Michael duPont"
__email__ = "michael@mdupont.com"
__license__ = "MIT"
__version__ = "1.2.2"
__stations__ = "2019-05-17"

setup(
    name="avwx-engine",
    version=__version__,
    description=__doc__,
    url="https://github.com/avwx-rest/AVWX-Engine",
    author=__author__,
    author_email=__email__,
    license=__license__,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">= 3.6",
    install_requires=[
        "aiohttp~=3.5",
        'dataclasses>=0.6;python_version<"3.7"',
        "python-dateutil~=2.8",
        "xmltodict~=0.12",
    ],
    packages=["avwx"],
    package_data={"avwx": ["aircraft.json", "stations.json"]},
    tests_require=["pytest-asyncio~=0.10"],
    extras_require={"scipy": ["scipy~=1.3"]},
)
