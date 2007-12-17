%define name	dhcpdump
%define version	1.7
%define release %mkrel 3

Summary:	Parse tcpdump DHCP packets
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        BSD
Group:		Networking/Other
URL:		http://www.mavetju.org/unix/general.php
Source:         http://www.mavetju.org/download/%{name}-%{version}.tar.bz2
Requires:	tcpdump

%description
A post-processor of tcpdump output to analyze sniffed DHCP
packets.

%prep

%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTACT
%{_bindir}/*
%{_mandir}/*/*


