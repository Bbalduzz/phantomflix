import setuptools, sys

with open("README.md", "r", encoding="utf-8") as fh: long_description = fh.read()

setuptools.setup(
    name="phantomflix",
    version="2023.1.4",
    author="Bbalduzz",
    description="Netflix API Metadata & Downloader for Windows and Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bbalduzz/phantomflix",
    project_urls={
        "Tracker": "https://github.com/Bbalduzz/phantomflix/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "protobuf",
        "pycryptodomex",
        "hyper @ git+https://github.com/tpubg583/hyper@development" if sys.version_info.major==3 and sys.version_info.minor>=10 else "hyper"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9.8",
)
