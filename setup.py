import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_voice_eaR",
    version="0.0.1",
    author="Rohan Lal Kshetry",
    author_email="rlkshetry95@gmail.com",
    description="A voice and take command package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rohan-LK/pc_voice_eaR",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
