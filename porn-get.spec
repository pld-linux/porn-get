Summary:	Advanced Package Tool for get sex-pictures from the net
Summary(pl):	Narzêdzie do ³atwego pobierania nieprzyzwoitych obrazków :-)
Name:		porn-get
Version:	0.5.1
Release:	0.1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.lesbian.mine.nu/%{name}_%{version}.tar.gz
# Source0-md5:	f283e1bfe40e38547344c4af617786b4
Patch0:		%{name}-filebyfile.patch
Patch1:		%{name}-INSTALL-ALL.patch
Patch2:		%{name}-PLD.patch
Patch3:		porn-cache-PLD.patch
Patch4:		%{name}-NewLocation.patch
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
%setup -q -n %{name}_%{version}
#%patch0 -p0
#%patch1 -p0
#%patch2 -p0
%patch3 -p0
#%patch4 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install	porn-get porn-cache $RPM_BUILD_ROOT%{_bindir}
install porn.1 $RPM_BUILD_ROOT%{_mandir}/man1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {readme,changelog}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
