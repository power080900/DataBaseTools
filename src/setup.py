import setuptools

with open("README.md","r", encoding='utf-8') as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = "What_your_EDA",
    version = "0.0.1",
    author = "KJLEE",
    author_email = "KJLee@dinsight.ai",
    description = "A small example package",
    long_description = long_description,
    long_description_content_type = "markdown",
    url= "" ,
    packages = setuptools.find_packages(),
    classifiers = [
        "Programing Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6' ,
)