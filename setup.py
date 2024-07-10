import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Deep Learning"
Author_USER_NAME = "HusnaMundambra"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "husnaakareem@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{Author_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)  