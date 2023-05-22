# -*- coding: utf-8 -*-
import setuptools

about = {}
with open("__about__.py") as fp:
    exec(fp.read(), about)

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    url="",
    license=about['__license__'],
    author="xxx",
    author_email="xxx",
    description=about['__description__'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    platforms=["any"],
)
