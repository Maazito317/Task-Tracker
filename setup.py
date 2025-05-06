# setup.py
from setuptools import setup, find_packages

setup(
    name="task-cli",
    version="0.1.0",
    python_requires=">=3.7",
    py_modules=["models", "task_manager", "main"],
    install_requires=[
        # any runtime deps here (none in this simple case)
    ],
    entry_points={
        "console_scripts": [
            # this says “when someone runs `task-cli`, invoke main.main()”
            "task-cli = main:main",
        ]
    },
    author="Your Name",
    description="A simple JSON-backed task tracker CLI",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
