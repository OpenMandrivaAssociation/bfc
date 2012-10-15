%define git	20121015

Name:		bfc
Version:	0.1
Release:	%{?git:0.git%{git}.}1
Summary:	An alternative ABF client
Group:		Development/Other
License:	GPLv3+
Source0:	%{name}-%{git}.tar.xz
BuildArch:	noarch

%description
Build Farm Client aka bfc is an alternative command line client for ABF
(Automated Build Farm). It is being under development and not feature-rich
yet.

%prep
%setup -qn %{name}-%{git}

%build
pod2man bfc > bfc.1

%install
install -D -m 755 bfc %{buildroot}%{_bindir}/bfc
install -D -m 644 bfc.1 %{buildroot}%{_mandir}/man1/bfc.1

%files
%doc README
%{_bindir}/bfc
%{_mandir}/man1/bfc.1*
