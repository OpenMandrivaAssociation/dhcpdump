Summary:	Parse tcpdump DHCP packets
Name:           dhcpdump
Version:        1.8
Release:        %mkrel 2
License:        BSD
Group:		Networking/Other
URL:		http://www.mavetju.org/unix/general.php
Source:         http://www.mavetju.org/download/%{name}-%{version}.tar.gz
Patch0:		dhcpdump-1.8.patch
Requires:	tcpdump
BuildRequires:	perl
BuildRequires:	pcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A post-processor of tcpdump output to analyze sniffed DHCP
packets.

%prep

%setup -q
%patch0 -p0 -b .build

%build

%make CCFLAGS="%{otpflags}"

%install
rm -rf %{buildroot}

install -D -m 755 dhcpdump %buildroot%_bindir/%{name}
install -D -m644 dhcpdump.8 %buildroot%_mandir/man8/dhcpdump.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTACT
%{_bindir}/*
%{_mandir}/*/*
