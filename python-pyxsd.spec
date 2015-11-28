%define 	module	pyxsd
Summary:	Python XML/Schema processing tool
Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	0.1
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/pyxsd/%{module}-0-1.tgz
# Source0-md5:	8f02162395a67956894efc4d1a2febda
URL:		http://pyxsd.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyXSD is a free, open source python program that maps xml and xsd(XML
Schema) files into python, allowing for easy schema-based validation
and transformation of xml files.

%description -l pl.UTF-8

%prep
%setup -q -c -n %{module}-%{version}

%build
# CFLAGS is only for arch packages - remove on noarch packages
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc
%attr(755,root,root) %{_bindir}/pyXSD.py
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
