from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing-test",
    version="0.0.1",
    author="Rafael de Brito",
    author_email="rafaeldebrito.ti@gmail.com",
    description="",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaeldb?tab=repositories",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
