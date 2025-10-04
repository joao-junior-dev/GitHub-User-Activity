from setuptools import setup, find_packages

setup(
    name="github-activity",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "git-activity=github_activity.__main__:main",
        ],
    },
)