#define git	20121105

Name:		bfc
Version:	0.2
Release:	%{?git:0.git%{git}.}7
Summary:	An alternative ABF client
Group:		Development/Other
License:	GPLv3+
URL:		https://github.com/mikhirev/bfc
%if 0%{?git}
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	%{name}-%{version}.tar.xz
%endif
Source1:	bfc.conf
Patch0:		bfc-0.2-git20121225.patch
BuildArch:	noarch
Requires:	perl(LWP::Protocol::https)
Requires:	perl-RPM
Requires:	rpm-build

%description
Build Farm Client aka bfc is an alternative command line client for ABF
(Automated Build Farm) and %{distribution} maintainers' helper.
It is being under development and not feature rich yet.

%prep
%setup -q %{?git: -n %{name}-%{git}}
%patch0 -p1

%build
pod2man bfc > bfc.1

%install
install -D -m 755 bfc %{buildroot}%{_bindir}/bfc
install -D -m 644 bfc.1 %{buildroot}%{_mandir}/man1/bfc.1
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bfc.conf

%files
%doc README
%{_bindir}/bfc
%{_mandir}/man1/bfc.1*
%config %{_sysconfdir}/bfc.conf
