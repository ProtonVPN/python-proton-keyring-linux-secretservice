%define unmangled_name proton-keyring-linux-secretservice
%define version 0.0.1
%define release 1

Prefix: %{_prefix}

Name: python3-%{unmangled_name}
Version: %{version}
Release: %{release}%{?dist}
Summary: %{unmangled_name} library

Group: ProtonVPN
License: GPLv3
Vendor: Proton Technologies AG <opensource@proton.me>
URL: https://github.com/ProtonVPN/%{unmangled_name}
Source0: %{unmangled_name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{unmangled_name}-%{version}-%{release}-buildroot

BuildRequires: gnome-keyring
BuildRequires: python3-setuptools
BuildRequires: python3-proton-keyring-linux
Requires: gnome-keyring
Requires: python3-proton-keyring-linux
Requires: gnome-keyring

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
* Tue Jun 28 2022 Proton Technologies AG <opensource@proton.me> 0.0.1
- First RPM release
