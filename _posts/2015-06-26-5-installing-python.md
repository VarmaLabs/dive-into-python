---
layout: post
title: Installing Python
order: 5
author: kpvarma
excerpt: "Know how to install python on Linux, MAC or Windows."
tags: [introduction, chapter-2]
comments: true
share: true
---
## Linux

The latest versions of Ubuntu and Fedora come with Python 2.7 out of the box.

The latest versions of Redhat Enterprise (RHEL) and CentOS come with Python 2.6. Some older versions of RHEL and CentOS come with Python 2.4 which is unacceptable for modern Python development. Fortunately, there are Extra Packages for Enterprise Linux which include high quality additional packages based on their Fedora counterparts. This repository contains a Python 2.6 package specifically designed to install side-by-side with the system’s Python 2.4 installation.

You do not need to install or configure anything else to use Python. Having said that, I would strongly recommend that you install the tools and libraries described in the next section before you start building Python applications for real-world use. In particular, you should always install Setuptools, as it makes it much easier for you to use other third-party Python libraries.

## MAC

The latest version of Mac OS X, Yosemite, comes with Python 2.7 out of the box.

You do not need to install or configure anything else to use Python. Having said that, I would strongly recommend that you install the tools and libraries described in the next section before you start building Python applications for real-world use. In particular, you should always install Setuptools, as it makes it much easier for you to use other third-party Python libraries.

The version of Python that ships with OS X is great for learning but it’s not good for development. The version shipped with OS X may be out of date from the official current Python release, which is considered the stable production version.

## Windows

There is a windows python installer which you can download [here](https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi). It comes as an MSI package. Double click the file and it will direct you through the installation steps. 

You will have to be an administrator to install Python on windows.

You can install multiple python versions on windows. Python by default installs the packages to a folder containing the version.

For e.g: 

	_C:/Python27_
	_C:/Python26_ etc

You should add _C:\Python27_ to **PATH** environment variable if you want Python 2.7 to be set to default.

### Setup Tools and Pip

Starting from Python versions 2.7.9 and 3.4.0, pip is already included in the regular install, see matth's answer below. Check if the path to the Scripts directory inside your Python installation directory is contained in your system's PATH environment variable, so pip can be found.

## Installing Python 3

You can download the Python 3 package from [here](https://www.python.org/downloads/).

Many system programs depends on Python 2 and not Python 3. Hence, it is not a good idea to make Python 3 as default.

You can run a script in Python 3 explicitly.

	python3 file.py

It's not good to change the default python. Many system programs depends on python2 not python3. if you want to use python3, you just type the command python3.

### References

* [http://docs.python-guide.org/en/latest/starting/install/win/](http://docs.python-guide.org/en/latest/starting/install/win/)
* [http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows)
* [http://askubuntu.com/questions/320996/make-default-python-command-to-use-python-3](http://askubuntu.com/questions/320996/make-default-python-command-to-use-python-3)
* [http://askubuntu.com/questions/103469/how-do-i-change-my-pythonpath-to-make-3-2-my-default-python-instead-of-2-7-2](http://askubuntu.com/questions/103469/how-do-i-change-my-pythonpath-to-make-3-2-my-default-python-instead-of-2-7-2)
