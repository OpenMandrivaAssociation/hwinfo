%define major	20
%define libname %mklibname hd %{major}
%define devname %mklibname -d hd

Summary:	Hardware Library
Name:		hwinfo
Version:	20.0
Release:	4
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://software.opensuse.org
# Source are generated for git
# git clone git://gitorious.org/opensuse/hwinfo.git
# pushd hwinfo && git checkout %{version} &&
# popd && tar -caf %{name}-%{version}.tar.gz  hwinfo
Source0:	%{name}-%{version}.tar.bz2
Patch1:		hwinfo-14.19-kbd.c-tiocgdev_undefined.patch
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Writer
BuildRequires:	udev
%ifarch %{ix86} x86_64
BuildRequires:	libx86emu-devel
%endif

%description
A simple program that lists results from the hardware detection
library.

%package -n %{libname}
Summary:	Libraies for %{name}
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}.

%package -n %{devname}
Summary:	Hardware Detection Library
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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
%doc README
%{_sbindir}/hwinfo
%{_sbindir}/mk_isdnhwdb
%{_sbindir}/getsysinfo
%dir %{_localstatedir}/lib/hardware
%dir %{_localstatedir}/lib/hardware/udi
%dir %{_datadir}/hwinfo
%{_datadir}/hwinfo/*
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/libhd.so.%{major}*

%files -n %{devname}
%doc doc/libhd/html
%{_sbindir}/check_hd
%{_sbindir}/convert_hd
%{_libdir}/libhd.so
%{_libdir}/pkgconfig/hwinfo.pc
%{_includedir}/hd.h

