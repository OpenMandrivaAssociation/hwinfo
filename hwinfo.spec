%define major 19
%define libname %mklibname hd %major
%define develname %mklibname -d hd

Name:           hwinfo
License:        GPLv2+
Group:          System/Kernel and hardware
Summary:        Hardware Library
Version:        19.1
Release:        1
Source0:        %{name}-%{version}.tar.bz2
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
%{_libdir}/libhd.so.%{major}*

%files -n %develname
%doc doc/libhd/html
%{_sbindir}/check_hd
%{_sbindir}/convert_hd
%{_libdir}/libhd.so
%{_libdir}/pkgconfig/hwinfo.pc
%{_includedir}/hd.h
