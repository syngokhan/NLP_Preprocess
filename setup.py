import setuptools

with open("README.md","r") as file:
    long_description = file.read()


setuptools.setup(
    name = "Preprocess_gokhanEr", # This should be unique
    version = "0.0.2",
    author = "Gokhan Ersoz",
    authoe_email = "syn_gokhan_85@hotmail.com",
    description = "This is preprocessing package",
    long_description = long_description,
    long_description_content_type = "text/markdown", # README.md Çünkü!!!!
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Aproved :: MIT License",
        "Operating System :: OS Independet" ],
    python_requires = ">=3.5"
    )