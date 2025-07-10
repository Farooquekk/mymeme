from setuptools import setup, find_packages

setup(
    name="mymeme",
    version="0.1.0",
    author="Farooque Sajjad",
    author_email="farooquekk92@gmail.com",
    description="A simple meme generator using Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Farooquekk/mymeme",
    license="MIT",
    packages=find_packages(),
    install_requires=["Pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
