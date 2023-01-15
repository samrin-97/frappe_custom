from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customize_app/__init__.py
from customize_app import __version__ as version

setup(
	name="customize_app",
	version=version,
	description="Customize App",
	author="Open Source",
	author_email="samreen486.SS@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
