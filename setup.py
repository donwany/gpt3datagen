from setuptools import setup, find_packages
from pathlib import Path

with open("README.md") as f:
    README = f.read()

here = Path(__file__).resolve().parent
VERSION = (here / "VERSION").read_text(encoding="utf-8").strip()

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

excluded_packages = ["docs", "tests", "tests.*"]

setup(
    name="gpt3datagen",
    py_modules=["gpt3datagen"],
    version=VERSION,
    description="Fine-Tune GPT-3 Data Generator is a python package that generate fake datasets.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Theophilus Siameh",
    author_email="theodondre@gmail.com",
    url="https://github.com/donwany/gpt3datagen",
    license="MIT License",
    install_requires=install_requires,
    packages=find_packages(exclude=excluded_packages),
    entry_points={
        "console_scripts": ["gpt3datagen=gpt3datagen.prepare:cli"],
    },
    classifiers=[
        # See https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    keywords="GPT3, GPT3 DataGen, Sample Faker, DataGen, Fine-Tune",
    platforms=["any"],
    python_requires=">=3.7",
)
