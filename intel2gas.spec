Summary:	intel2gas is a x86 assembly source converter
Name:		intel2gas
Version:	1.3.2
Release:	1
License:	GPL
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://www.niksula.cs.hut.fi/~mtiihone/intel2gas/%{name}-%{version}.tar.gz
Patch0:		intel2gas-DESTDIR.patch
URL:		http://www.niksula.cs.hut.fi/~mtiihone/intel2gas/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program converts your assembly source files from NASM to gas or
the other way around so you don't have to have the other assembler to
build them.

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates"
export LDFLAGS CXXFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BUGS ChangeLog DATAFILES README THANKS TODO

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/intel2gas
%{_datadir}/intel2gas
