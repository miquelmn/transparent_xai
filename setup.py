from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as fp:
    install_requires = fp.read()

setup(
    name="transparent_xai",
    version="1.0.0",
    description="From transparent models to local explanation",
    #url="https://github.com/explainingAI/uib-xai",
    author="Dr. Miquel Miró Nicolau, Dr. Gabriel Moyà Alcover, Dr. Antoni Jaume-i-Capó",
    author_email="miquel.miro@uib.cat",
    license="MIT",
    packages=["transparent_XAI"],
    keywords=[
        "Explainable artificial intelligence",
    ],
    install_requires=install_requires,
    python_requires=">=3.8",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
)
