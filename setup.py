import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = '0.0.1'

REPONAME = 'End-To-End-Wine-Quality'
AUTHOR_USER_NAME = 'naamShahreyar'
SRC_REPO = 'WineQuality'
AUTHOR_EMAIL = 'shahreyar1411@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small package to predict wine quality',
    long_description=long_description,
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPONAME}',
    project_urls={
        "Bug Tracker": f'https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues',
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)