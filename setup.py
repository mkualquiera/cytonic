import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cytonic",
    version="0.0.1",
    author="mkualquiera",
    author_email="ozjuanpa@gmail.com",
    description="Flask/JS framework for calculator applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkualquiera/cytonic",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy>=1.19.5",
        "Flask>=1.1.2"
    ]
)