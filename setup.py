from setuptools import setup, find_packages

setup(
    name="thunderpuff",
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        thunderpuff-make=thunderpuff.scripts.make:main
    """,
)
