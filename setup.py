import setuptools

__version__ = "0.0.0"

REPO_NAME = "MLOPS-Project"
AUTHOR_USERNAME = 'InspectorGoole'
SRC_REPO = "mlproject" # folder at src folder

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    description="a small python package for ml app",
    url = f'https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)