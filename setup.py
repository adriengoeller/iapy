import sys
from pathlib import Path
from typing import List

projet_dir: Path = Path(__file__).resolve().parent
source_dir: Path = projet_dir / "src"
sys.path.insert(0,str(source_dir))

from iapy import LICENCE, AUTHOR, AUTHOR_EMAIL, PROJECT, DESCRIPTION, __version__ as VERSION

from setuptools import setup, find_packages


def parse_requirements(filename: str) -> List[str]:
    """Load requirements from pip requirements file"""
    with open(filename, "r") as f:
        lines: List[str] = []
        for l in f:
            l.strip()
            if l and not l.startswith('#'):
                lines.append(l)
    return lines

requirements: List[str] = parse_requirements("requirements.txt")

if __name__ == "__main__":
    setup(
        name=PROJECT,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        install_requires=requirements,
        keywords=['iapy'],
        packages=find_packages(source_dir),
        package_dir= {"iapy":source_dir / "iapy"},
        url='https://github.com/adriengoeller/iapy', 
        python_requires='>=3',
        license='LICENSE', 
        description=DESCRIPTION,
        long_description=open('README.md').read(),
        )
    