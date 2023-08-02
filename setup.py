import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_des = file.read()

__version__ = "0.0.0"

REPO_NAME = "machine-learning-with-mlflow"
AUTHOR_USER_NAME = "abdullahkhan70"
SRC_REPO = "ml_project"
AUTHOR_EMAIL = "abdullahkhan9003@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is just an example python package for ml app (specially for portfolio purposes)",
    long_description=long_des,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
