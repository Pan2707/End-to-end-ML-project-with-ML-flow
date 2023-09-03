#here we metion about  our local package installation
#it will look everywhere for the constructor file and install the folder as the local package

# to install setup.py, we need to have -e . file in requirements.txt file


import setuptools

with open("README.md", "r", encoding="utf-8") as f: # opens our README file
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "Pandeyprashant"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "pandeyprashant895@gmail.com"

#here is the setup file
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)


