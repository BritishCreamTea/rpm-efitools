Name:           efitools
Version:        1.8.1
Release:        2%{?dist}
Summary:        Tools for manipulating efi platorms.
Group:          Applications/System
License:        GPL
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/snapshot/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gcc
BuildRequires:  sbsigntools
BuildRequires:  gnu-efi-devel
BuildRequires:  binutils-devel
BuildRequires:  openssl-devel
Requires: openssl

%description
The efitools package provides many useful tools for managing efi systems.

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT
make clean

%files
%defattr(-,root,root,-)
%license COPYING
%doc README
%{_bindir}/*
%{_mandir}/man1/*
%{_datarootdir}/efitools/*


%changelog
* Tue Dec 11 2018 Daniel Dawson <35599367+D-Dawson@users.noreply.github.com> - 1.8.1-2
- Initial RPM Build

