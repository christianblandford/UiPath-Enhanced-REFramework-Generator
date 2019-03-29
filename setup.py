import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uipath_enhanced_reframework_generator",
    version="0.0.5",
    author="Christian Blandford",
    author_email="christianblandford@me.com",
    description="Generator to scaffold a new Enhanced REFramework project.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/christianblandford/UiPath-Scaffold",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "console_functions >= 0.0.8",
        "uipath_scaffold >= 0.0.1",
        "uipath_scaffold_generator >= 0.0.1",
        "uipath >= 0.0.1"
    ],
)
