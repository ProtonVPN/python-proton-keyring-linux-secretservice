%define unmangled_name proton-keyring-linux-secretservice
%define version 0.0.2
%define release 1

Prefix: %{_prefix}

Name: python3-%{unmangled_name}
Version: %{version}
Release: %{release}%{?dist}
Summary: %{unmangled_name} library

Group: ProtonVPN
License: GPLv3
Vendor: Proton AG <opensource@proton.me>
URL: https://github.com/ProtonVPN/python-%{unmangled_name}
Source0: %{unmangled_name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{unmangled_name}-%{version}-%{release}-buildroot

BuildRequires: gnome-keyring
BuildRequires: python3-setuptools
BuildRequires: python3-proton-keyring-linux
BuildRequires: python3-secretstorage
Requires: gnome-keyring
Requires: python3-proton-keyring-linux
Requires: python3-secretstorage

%{?python_disable_dependency_generator}

%description
Package %{unmangled_name} library.


%prep
%setup -n %{unmangled_name}-%{version} -n %{unmangled_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES


%files -f INSTALLED_FILES
%{python3_sitelib}/proton/
%{python3_sitelib}/proton_keyring_linux_secretservice-%{version}*.egg-info/
%defattr(-,root,root)

%changelog
* Wed Mar 20 2024 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.0.2
- Ensure data is properly parsed when it is fetched without a keyring password due to a bug with gnome-keyring
- https://discourse.gnome.org/t/possible-bug-or-feature-storing-getting-data-keyring-protected-vs-unprotected-keyring/20312

* Tue Jun 28 2022 Proton Technologies AG <opensource@proton.me> 0.0.1
- First RPM release
