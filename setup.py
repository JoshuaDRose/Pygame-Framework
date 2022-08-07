import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="projectname",
    version="0.0.1",
    author="John Doe",
    author_email='jdoe@example.com',
    description="My short description",
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-clarity",
            'mock;python_version<"3.3"']
    },
    install_requires=["PyYAML"],
    url="https://github.com/JoshuaDRose/Pygame-Framework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
