Name:		python-librt
Version:	0.7.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/l/librt/librt-%{version}.tar.gz
Summary:	Mypyc runtime library
URL:		https://pypi.org/project/librt/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python

%description
Mypyc runtime library

%files
%{py_platsitedir}/librt
%{py_platsitedir}/librt-%{version}.dist-info
