from setuptools import setup, find_packages

setup(
    name="snippeter",
    version="0.1.0",
    description="A CLI tool for managing C++ code snippets",
    author="Your Name",
    py_modules=["cli", "snippets"],
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "pyperclip>=1.8.2",
        "thefuzz>=0.20.0",
        "python-Levenshtein>=0.21.0",
        "InquirerPy>=0.3.4",
    ],
    entry_points={
        "console_scripts": [
            "snippeter=cli:app",
        ],
    },
    python_requires=">=3.7",
)
