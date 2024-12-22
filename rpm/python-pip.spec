Name:           python-pip
# When updating, update the bundled libraries versions bellow!
Version:        23.3.2
Release:        1
Summary:        A tool for installing and managing Python packages

# We bundle a lot of libraries with pip, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:

# appdirs: MIT
# certifi: MPLv2.0
# chardet: LGPLv2
# colorama: BSD
# CacheControl: ASL 2.0
# distlib: Python
# distro: ASL 2.0
# html5lib: MIT
# idna: BSD
# ipaddress: Python
# msgpack: ASL 2.0
# packaging: ASL 2.0 or BSD
# progress: ISC
# pygments: BSD
# pyparsing: MIT
# pyproject-hooks: MIT
# requests: ASL 2.0
# resolvelib: ISC
# rich: MIT
# setuptools: MIT
# six: MIT
# tenacity: ASL 2.0
# truststore: MIT
# tomli: MIT
# typing-extensions: Python
# urllib3: MIT
# webencodings: BSD

License:        MIT and Python and ASL 2.0 and BSD and ISC and LGPLv2 and MPLv2.0 and (ASL 2.0 or BSD)
URL:            https://github.com/sailfishos/python-pip
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
pip is a package management system used to install and manage software packages
written in Python. Many packages can be found in the Python Package Index
(PyPI). pip is a recursive acronym that can stand for either "Pip Installs
Packages" or "Pip Installs Python".


# Virtual provides for the packages bundled by pip.
# You can find the versions in src/pip/_vendor/vendor.txt file.
%global bundled() %{expand:
Provides: bundled(python%{1}dist(CacheControl)) = 0.13.1
Provides: bundled(python%{1}dist(certifi)) = 2023.7.22
Provides: bundled(python%{1}dist(chardet)) = 5.1.0
Provides: bundled(python%{1}dist(colorama)) = 0.4.6
Provides: bundled(python%{1}dist(distlib)) = 0.3.6
Provides: bundled(python%{1}dist(distro)) = 1.8.0
Provides: bundled(python%{1}dist(idna)) = 3.4
Provides: bundled(python%{1}dist(msgpack)) = 1.0.5
Provides: bundled(python%{1}dist(packaging)) = 21.3
Provides: bundled(python%{1}dist(platformdirs)) = 3.8.1
Provides: bundled(python%{1}dist(pygments)) = 2.15.1
Provides: bundled(python%{1}dist(pyparsing)) = 3.1.0
Provides: bundled(python%{1}dist(pyproject-hooks)) = 1.0.0
Provides: bundled(python%{1}dist(requests)) = 2.31.0
Provides: bundled(python%{1}dist(resolvelib)) = 1.0.1
Provides: bundled(python%{1}dist(rich)) = 13.4.2
Provides: bundled(python%{1}dist(setuptools)) = 68.0.0
Provides: bundled(python%{1}dist(six)) = 1.16.0
Provides: bundled(python%{1}dist(tenacity)) = 8.2.2
Provides: bundled(python%{1}dist(tomli)) = 2.0.1
Provides: bundled(python%{1}dist(truststore)) = 0.8.0
Provides: bundled(python%{1}dist(typing_extensions)) = 4.7.1
Provides: bundled(python%{1}dist(urllib3)) = 1.26.17
Provides: bundled(python%{1}dist(webencodings)) = 0.5.1
}


%package -n python3-pip
Summary:        A tool for installing and managing Python3 packages

BuildRequires:  python3-devel
# python3 bootstrap: this is rebuilt before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manuallyl
BuildRequires:  python3-rpm-generators
BuildRequires:  python3-setuptools

# Virtual provides for the packages bundled by pip:
%{bundled 3}

%description -n python3-pip
pip is a package management system used to install and manage software packages
written in Python. Many packages can be found in the Python Package Index
(PyPI). pip is a recursive acronym that can stand for either "Pip Installs
Packages" or "Pip Installs Python".

%prep
%autosetup -p1 -n %{name}-%{version}/pip

%build
%py3_build

%install
%py3_install

# Provide symlinks to executables to comply with Fedora guidelines for Python
ln -s ./pip%{python3_version} %{buildroot}%{_bindir}/pip-%{python3_version}
ln -s ./pip-%{python3_version} %{buildroot}%{_bindir}/pip-3

%files -n python3-pip
%license LICENSE.txt
%{_bindir}/pip
%{_bindir}/pip3
%{_bindir}/pip-3
%{_bindir}/pip%{python3_version}
%{_bindir}/pip-%{python3_version}
%{python3_sitelib}/pip*
