from setuptools import setup, find_packages

setup(
    name="depth-anything",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    # Optionally, if you have any package data to include
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # And include any files found in the "data" subdirectory of the "mypkg" package, also:
        "mypkg": ["data/*"],
    },
)
