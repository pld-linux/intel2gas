Summary:	intel2gas is a x86 assembly source converter
Summary(pl):	Konwerter kodu ¼ród³owego w asemblerze x86
Name:		intel2gas
Version:	1.3.3
Release:	5
License:	GPL
Group:		Development/Tools
Source0:	http://www.niksula.cs.hut.fi/~mtiihone/intel2gas/%{name}-%{version}.tar.gz
Source1:	%{name}.1
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.niksula.cs.hut.fi/~mtiihone/intel2gas/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program converts your assembly source files from NASM to gas or
the other way around so you don't have to have the other assembler to
build them.

%description -l pl
Ten program konwertuje pliki ¼ród³owe w asemblerze ze sk³adni NASM do
gas lub odrotnie.

%prep
%setup -q
%patch -p1

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

gzip -9nf BUGS ChangeLog DATAFILES README THANKS TODO

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/intel2gas
%{_datadir}/intel2gas
%{_mandir}/man1/intel2gas.1*
