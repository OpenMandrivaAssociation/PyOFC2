%define unmangled_version 0.1.5dev

Summary: Python library for Open Flash Chart 2
Name:    PyOFC2
Version: 0.1.5dev
Release: 4
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Python
Prefix: %{_prefix}
BuildArch: noarch
Url: http://pradeepgowda.com/
AutoReq: 0

BuildRequires: python-devel python-setuptools

%description
PyOFC2 - Python libraries for Open Flash Chart
==============================================

PyOFC2 generates data files required for `Open Flash Chart 2
<http://teethgrinder.co.uk/open-flash-chart-2/>`_.

Installation
------------

Using `Python Packaging Index <http://pypi.python.org>`_:

    $ easy_install PyOFC2
    
From the source:

    $ git://github.com/btbytes/pyofc2.git
    
Online `Demo <http://btbytes.github.com/pyofc2/>`_.


Using PyOFC2 with Web Frameworks
--------------------------------
`Django + PyOFC2 <http://github.com/btbytes/djofc2_demo>`_ example project.

     

NEWS
====

0.1.5
-----

*Release Date: 2010-09-21*

* Fixed setup bug. Thx http://github.com/marcinn


0.1.4
-----
*Release Date: 2010-09-21*

* converted README to `.rst`. Added `NEWS.rst` for project release information. 
* better pypi documentation.


0.1.3
-----
*Release Date: 2010-09-21*

* Added `bar_on_show` option. Thanks to `lukaszb <http://github.com/lukaszb>`_.


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
#python setup.py install --single-version-externally-managed --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
python setup.py install  --root=%{buildroot} --record=INSTALLED_FILES

# Sort the filelist so that directories appear before files. This avoids
# dublicate filename problems on some systems
touch DIRS
for i in `cat INSTALLED_FILES`; do
    if [ -f %{buildroot}/$i ]; then
	echo $i >>FILES
    fi
    if [ -d %{buildroot}/$i ]; then
	echo %dir $i >>DIRS
    fi
done

# Make sure we match f00.pyo and foo.pyc along with foo.py (but only once each)
sed -e "/\.py[co]$/d" -e "s/\.py$/.py*/" DIRS FILES >INSTALLED_FILES

%files -f INSTALLED_FILES
#%{py_sitedir}/pyofc2/__init__.py
#/usr/lib/python2.6/site-packages/pyofc2/ofc2.py

%changelog
* Wed Dec 07 2011 Pischulin Anton <apischulin@mandriva.org> 0.1.5dev-1
+ Revision: 738480
- add PyOFC2 sources

