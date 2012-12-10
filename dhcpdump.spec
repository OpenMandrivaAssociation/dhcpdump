Summary:	Parse tcpdump DHCP packets
Name:           dhcpdump
Version:        1.8
Release:        %mkrel 4
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8-4mdv2011.0
+ Revision: 617578
- the mass rebuild of 2010.0 packages

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.8-3mdv2010.0
+ Revision: 453452
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8-2mdv2009.1
+ Revision: 298237
- rebuilt against libpcap-1.0.0

* Tue Aug 12 2008 Olivier Thauvin <nanardon@mandriva.org> 1.8-1mdv2009.0
+ Revision: 271012
- buildrequires
- 1.8

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.7-5mdv2009.0
+ Revision: 244083
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.7-3mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org> 1.7-3mdv2007.0
+ Revision: 53227
- rebuild
- Import dhcpdump

* Tue Dec 20 2005 Olivier Thauvin <nanardon@mandriva.org> 1.7-2mdk
- %%{1}mdv2007.1
- rebuild

* Mon Nov 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.7-1mdk
- 1.7
- make it rpmbuildupdate aware

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.6-1mdk
- 1.6
- use macros

