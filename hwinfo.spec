%define major 20
%define libname %mklibname hd %major
%define develname %mklibname -d hd

Name:           hwinfo
License:        GPLv2+
Group:          System/Kernel and hardware
Summary:        Hardware Library
Version:        20.0
Release:        1
# Source are generated for git
# git clone git://gitorious.org/opensuse/hwinfo.git
# pushd hwinfo && git checkout %{version} &&
# popd && tar -caf %{name}-%{version}.tar.gz  hwinfo
Source:         %{name}-%{version}.tar.bz2
Patch1:		hwinfo-14.19-kbd.c-tiocgdev_undefined.patch
URL:		http://software.opensuse.org
Requires:	%{libname} = %{version}-%{release}
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Writer
BuildRequires:	udev
%ifarch %{ix86} x86_64
BuildRequires:	libx86emu-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
A simple program that lists results from the hardware detection
library.

%package -n %{libname}
Summary:	Libraies for %{name}
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}.

%package -n %{develname}
Summary:        Hardware Detection Library
Group:          Development/Other
Requires:       %libname = %version-%release
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libhd-devel = %{version}-%{release}

%description -n %{develname}
This library collects information about the hardware installed on a
system.

%prep
%setup -q
%patch1 -p0 -b .undefined

%build
make LIBDIR=%{_libdir} LDFLAGS="%{optflags} -Lsrc"
make doc

%install
%makeinstall_std LIBDIR=%{_libdir}

install -d -m 755 %{buildroot}%{_mandir}/man8
install -m 644 doc/hwinfo.8 %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_var}/lib/hardware/udi

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/hwinfo
%{_sbindir}/mk_isdnhwdb
%{_sbindir}/getsysinfo
%{_mandir}/man8/*
%dir %{_localstatedir}/lib/hardware
%dir %{_localstatedir}/lib/hardware/udi
%dir %{_datadir}/hwinfo
%{_datadir}/hwinfo/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libhd.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc doc/libhd/html
%{_sbindir}/check_hd
%{_sbindir}/convert_hd
%{_libdir}/libhd.so
%{_libdir}/pkgconfig/hwinfo.pc
%{_includedir}/hd.h


%changelog
* Thu Oct 09 2012 Alexander Kazancev <kazancas@mandriva.org> 20.0-1
- version update 20.0

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 18.5-2mdv2011.0
+ Revision: 665488
- mass rebuild

* Tue Mar 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 18.5-1
+ Revision: 647686
- drop ancient ldconfig scriptlet
- make buildrequires on libx86emu-devel conditional

  + Matthew Dawkins <mattydaw@mandriva.org>
    - new version 18.5 rebased from opensuse
    - drops hal dependency

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 16.0-3mdv2011.0
+ Revision: 605887
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 16.0-2mdv2010.1
+ Revision: 522888
- rebuilt for 2010.1

* Wed Jun 10 2009 Frederik Himpe <fhimpe@mandriva.org> 16.0-1mdv2010.0
+ Revision: 384920
- Update to new version 16.0
- Use Debian source and URL so that it can be updated with mdvsys update

  + Funda Wang <fwang@mandriva.org>
    - rediff patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 14.19-1mdv2009.0
+ Revision: 216968
- use ldflags
- New version 14.19

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 13.57-1mdv2008.1
+ Revision: 100828
- New version 13.57

* Fri Oct 12 2007 Funda Wang <fwang@mandriva.org> 13.54-1mdv2008.1
+ Revision: 97270
- New version 13.54

* Thu Sep 06 2007 Funda Wang <fwang@mandriva.org> 13.48-1mdv2008.0
+ Revision: 80627
- New version 13.48

* Tue Aug 21 2007 Funda Wang <fwang@mandriva.org> 13.45-1mdv2008.0
+ Revision: 68735
- New version 13.45

* Sun Jul 22 2007 Funda Wang <fwang@mandriva.org> 13.38-1mdv2008.0
+ Revision: 54423
- add ldconfig for libname
- fix rpm groups
- corrected libname
- Add debian patch to get it build in non-suse distro
- Import hwinfo
- Created package structure for hwinfo.

