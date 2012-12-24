#define git	20121105

Name:		bfc
Version:	0.2
Release:	%{?git:0.git%{git}.}2
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
BuildArch:	noarch
Requires:	perl(LWP::Protocol::https)

%description
Build Farm Client aka bfc is an alternative command line client for ABF
(Automated Build Farm) and %{distribution} maintainers' helper.
It is being under development and not feature rich yet.

%prep
%setup -q %{?git: -n %{name}-%{git}}

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
%config(noreplace) %{_sysconfdir}/bfc.conf
