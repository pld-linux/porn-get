Summary:	Advanced Package Tool for get sex-pictures from the net
Summary(pl):	Narzêdzie do ³atwego pobierania nieprzyzwoitych obrazków :-)
Name:		porn-get
Version:	0.4.0
Release:	2
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	http://www.linuks.mine.nu/porn-get/%{name}-%{version}.tar.bz2
Patch0:		%{name}-filebyfile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	bash
Requires:	wget
Requires:	lynx
BuildArch:	noarch

%description
Sexual education is important for humanity.

%description -l pl
Wiedza o seksie jest bardzo wa¿na dla spo³eczeñstwa.

%prep
%setup -q
%patch -p0

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install	porn-get	$RPM_BUILD_ROOT%{_bindir}
install porn-cache 	$RPM_BUILD_ROOT%{_bindir}
install porn.1	$RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf {readme,changelog}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%doc readme.gz changelog.gz
