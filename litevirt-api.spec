%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:		litevirt-api
Version:	0.1.0
Release:	10000
Summary:	Litevirt RESTful API services
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Group:		Applications/System
License:	GPLv2+
URL:		www.litevirt.com
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	python-setuptools python-devel automake autoconf
Requires:       python-mimeparse
Requires:       python-gevent
Requires:       python-webpy

BuildArch:      noarch

%description
Provides RESTful API services for litevirt

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{python_sitelib}/mimerender
%{python_sitelib}/LitevirtAPI
%{_libexecdir}/litevirt-api-server

%doc README

%changelog
* Tue Aug 30 2012 Hao Luo <hluo@litevirt.com> - 0.1.0
- Initialize litevirt-api package

