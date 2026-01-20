from setuptools import setup

setup(
    name="caesar-cli",
    version="1.0",
    py_modules=["caesar"],  # name of your script without .py
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "caesar=caesar:main"  # "caesar" will become the command
        ]
    }
)
