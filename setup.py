# setup.py
from airflow_tf import __version__
import setuptools
import platform

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    _requirements = fh.read()

system_platform = platform.system()

setuptools.setup(
    name="airflow-tf",
    version=__version__,
    author="KnowAI",
    author_email="dev.know.ai@gmail.com",
    description="This package helps to integrate Tensorflow model development with Apache Airflow Pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU AFFERO GENERAL PUBLIC LICENSE",
    url="https://github.com/know-ai/airflow-tf",
    package_data={},
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=_requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: DeepLearning",
        "Topic :: System :: TensorFlow"
    ]
)
