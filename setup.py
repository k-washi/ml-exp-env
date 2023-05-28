from setuptools import find_packages, setup

setup(
    name="ml env",
    version="0.0.1",
    description="ml env",
    author="Kai Washizaki",
    author_email="bandad.kw@gmail.com",
    long_description_content_type="text/markdown",
    package_data={"": ["_example_data/*"]},
    packages=find_packages(include=["src*", "tests*"]),
    include_package_data=True,
)