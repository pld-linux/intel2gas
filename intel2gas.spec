%define name    intel2gas
%define version 1.3.2
%define release 1

Summary:   intel2gas is a x86 assembly source converter.
Name:      %{name}
Version:   %{version}
Release:   %{release}
Copyright: GPL
Group:     Development/Tools
Source:    http://hermes.terminal.at/intel2gas/%{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}

%description
This program converts your assembly source files from NASM to gas or the
other way around so you don't have to have the other assembler to build
them.

%prep
%setup -q
%configure

%build
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/intel2gas
make prefix=$RPM_BUILD_ROOT/usr install

%files
%defattr(-,root,root)
%doc BUGS COPYING ChangeLog DATAFILES README THANKS TODO
/usr/bin/intel2gas
/usr/share/intel2gas/*
