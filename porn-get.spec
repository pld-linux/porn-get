Summary:	Advanced Package Tool for get sex-pictures from the net
Summary(pl):	Narzêdzie do ³atwego pobierania nieprzyzwoitych obrazków :-)
Name:		porn-get
Version:	0.4.0
Release:	5
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	http://www.linuks.mine.nu/porn-get/%{name}-%{version}.tar.bz2
Patch0:		%{name}-filebyfile.patch
Patch1:		%{name}-INSTALL-ALL.patch
Patch2:		%{name}-PLD.patch
Patch3:		porn-cache-PLD.patch
Requires:	bash
Requires:	fileutils
Requires:	findutils
Requires:	grep
Requires:	lynx
Requires:	sed
Requires:	sh-utils
Requires:	textutils
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sexual education is important for humanity.

%description -l pl
Wiedza o seksie jest bardzo wa¿na dla spo³eczeñstwa.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install	porn-get porn-cache $RPM_BUILD_ROOT%{_bindir}
install porn.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf {readme,changelog}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
