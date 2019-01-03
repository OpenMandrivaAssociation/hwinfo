%define major 21
%define libname %mklibname hd %{major}
%define devname %mklibname -d hd

Summary:	Hardware Library
Name:		hwinfo
Version:	21.63
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		https://github.com/openSUSE/hwinfo
# Source are generated for git
# git clone https://github.com/openSUSE/hwinfo.git
# pushd hwinfo && git checkout %{version} &&
# popd && tar -caf %{name}-%{version}.tar.gz  hwinfo
Source0:	https://codeload.github.com/openSUSE/hwinfo/%{name}-%{version}.tar.gz
Patch0:		remove-git2log-and-references.patch
Patch1:		hwinfo-14.19-kbd.c-tiocgdev_undefined.patch
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(XML::Writer)
BuildRequires:	pkgconfig(libudev)
%ifarch %{ix86}	%{x86_64}
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
%autopatch -p1
echo %{version} > VERSION

%build
%global optflags %{optflags} -Qunused-arguments
%setup_compile_flags
%make_build shared CC=%{__cc} LIBDIR=%{_libdir} RPM_OPT_FLAGS="%{optflags}" LDFLAGS="%{ldflags} -Lsrc" -j1
#make doc

%install
%make_install LIBDIR=%{_libdir}

#install -d -m 755 %{buildroot}%{_mandir}/man8
#install -m 644 doc/hwinfo.8 %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_var}/lib/hardware/udi

%files
%{_sbindir}/hwinfo
%{_sbindir}/mk_isdnhwdb
%{_sbindir}/getsysinfo
%dir %{_localstatedir}/lib/hardware
%dir %{_localstatedir}/lib/hardware/udi
%dir %{_datadir}/hwinfo
%{_datadir}/hwinfo/*
#{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/libhd.so.%{major}*

%files -n %{devname}
%doc doc/libhd/html
%{_sbindir}/check_hd
%{_sbindir}/convert_hd
%{_libdir}/libhd.so
%{_libdir}/pkgconfig/hwinfo.pc
%{_includedir}/hd.h
