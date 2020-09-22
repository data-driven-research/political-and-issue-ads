import io
from setuptools import find_packages, setup


VERSION = "0.1.0"
with io.open("README.md", "rt", encoding="utf8") as f:
    LONG_DESC = f.read()


setup(
    name="src",
    packages=find_packages(),
    version=VERSION,
    description="Short desc",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    author="Hryhorii Pavlenko",
    author_email="hryhorii.pavlenko@gmail.com",
    license="MIT",
)
