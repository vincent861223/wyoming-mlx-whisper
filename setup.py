#!/usr/bin/env python3
from pathlib import Path

import setuptools
from setuptools import setup

this_dir = Path(__file__).parent

requirements = []
requirements_path = this_dir / "requirements.txt"
if requirements_path.is_file():
    with open(requirements_path, "r", encoding="utf-8") as requirements_file:
        requirements = requirements_file.read().splitlines()

module_name = "wyoming_mlx_whisper"
module_dir = this_dir / module_name
data_files = []

version_path = module_dir / "VERSION"
data_files.append(version_path)
version = version_path.read_text(encoding="utf-8").strip()

# -----------------------------------------------------------------------------

setup(
    name=module_name,
    version=version,
    description="Wyoming Server for MLX whisper",
    url="https://github.com/vincent861223/wyoming-mlx-whisper.git",
    author="Vincent Lin",
    author_email="wyoming_mlx_whisper@random.re",
    license="MIT",
    packages=setuptools.find_packages(),
    package_data={module_name: [str(p.relative_to(module_dir)) for p in data_files]},
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="rhasspy wyoming mlx whisper stt",
    entry_points={
        "console_scripts": ["wyoming-whisper-mlx-whisper = wyoming_mlx_whisper.__main__:run"]
    },
)
