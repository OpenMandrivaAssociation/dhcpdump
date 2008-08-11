%define name	dhcpdump
%define version	1.8
%define release %mkrel 1

Summary:	Parse tcpdump DHCP packets
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        BSD
Group:		Networking/Other
URL:		http://www.mavetju.org/unix/general.php
Source:         http://www.mavetju.org/download/%{name}-%{version}.tar.gz
Patch0: dhcpdump-1.8.patch
Requires:	tcpdump
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
A post-processor of tcpdump output to analyze sniffed DHCP
packets.

%prep

%setup -q
%patch0 -p0 -b .build

%build

%make CCFLAGS="%{otpflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -D -m 755 dhcpdump %buildroot%_bindir/%{name}
install -D -m644 dhcpdump.8 %buildroot%_mandir/man8/dhcpdump.8

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTACT
%{_bindir}/*
%{_mandir}/*/*

