Summary:	intel2gas is a x86 assembly source converter
Summary(pl.UTF-8):	Konwerter kodu źródłowego w asemblerze x86
Name:		intel2gas
Version:	1.3.3
Release:	7
License:	GPL
Group:		Development/Tools
Source0:	http://www.niksula.cs.hut.fi/~mtiihone/intel2gas/%{name}-%{version}.tar.gz
# Source0-md5:	40c85d961f6214903d80dc7f233a2c6f
Source1:	%{name}.1
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.niksula.cs.hut.fi/~mtiihone/intel2gas/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program converts your assembly source files from NASM to gas or
the other way around so you don't have to have the other assembler to
build them.

%description -l pl.UTF-8
Ten program konwertuje pliki źródłowe w asemblerze ze składni NASM do
gas lub odwrotnie.

%prep
%setup -q
%patch -P0 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog DATAFILES README THANKS TODO
%attr(755,root,root) %{_bindir}/intel2gas
%{_datadir}/intel2gas
%{_mandir}/man1/intel2gas.1*
