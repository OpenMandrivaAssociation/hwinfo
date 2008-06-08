%define major 14
%define libname %mklibname hd %major
%define develname %mklibname -d hd

Name:           hwinfo
License:        GPLv2+
Group:          System/Kernel and hardware
Summary:        Hardware Library
Version:        14.19
Release:        %mkrel 1
Source:         %{name}-%{version}.tar.bz2
Patch1:		hwinfo-13.38-kbd.c-tiocgdev_undefined.patch
URL:		http://ftp.opensuse.org/pub/opensuse/distribution/SL-OSS-factory/inst-source/suse/src/
Requires:	%{libname} = %{version}-%{release}
BuildRequires:  doxygen flex hal-devel perl-XML-Parser perl-XML-Writer udev
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
A simple program that lists results from the hardware detection
library.

%package -n %{libname}
Summary:	Libraies for %{name}
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

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
%patch1 -p0

%build
make LIBDIR=%{_libdir} LDFLAGS="-Wl,--as-needed -Wl,--no-undefined"
make doc

%install
%makeinstall_std LIBDIR=%{_libdir}

install -d -m 755 %{buildroot}%{_mandir}/man8
install -m 644 doc/hwinfo.8 %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_var}/lib/hardware/udi

%clean 
rm -rf %{buildroot}

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
