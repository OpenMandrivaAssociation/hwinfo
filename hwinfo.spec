%define libname %mklibname hwinfo 13
%define develname %mklibname -d hwinfo

Name:           hwinfo
License:        GPL v2 or later
Group:          Hardware/Other
Summary:        Hardware Library
Version:        13.38
Release:        %mkrel 1
Source:         %{name}-%{version}.tar.bz2
Requires:	%{libname} = %{version}-%{release}
BuildRequires:  doxygen flex hal-devel perl-XML-Parser perl-XML-Writer udev
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
A simple program that lists results from the hardware detection
library.

%package -n %{libname}
Summary:	Libraies for %{name}
Group:		System/Libries

%description -n %{libname}
Libraries for %{name}.

%package -n %{develname}
Summary:        Hardware Detection Library
Group:          Development/Libraries/C and C++
Requires:       %libname = %version-%release

%description -n %{develname}
This library collects information about the hardware installed on a
system.

%prep
%setup

%build
make LIBDIR=%{_libdir}
make doc

%install
%makeinstall_std LIBDIR=%{_libdir}

install -d -m 755 %{buildroot}%{_mandir}/man8
install -m 644 hwinfo.8 %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_var}/lib/hardware/udi

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/hwinfo
%{_sbindir}//mk_isdnhwdb
%{_sbindir}/getsysinfo
%{_mandir}/man8/*
%dir %{_var}/lib/hardware
%dir %{_var}/lib/hardware/udi
%dir %{_datadir}/hwinfo
%{_datadir}/hwinfo/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libhd.so.*

%files -n %develname
%defattr(-,root,root)
%doc doc/libhd/html
%{_sbindir}/check_hd
%{_sbindir}/convert_hd
%{_libdir}/libhd.so
%{_libdir}/libhd.a
%{_libdir}/pkgconfig/hwinfo.pc
%{_includedir}/hd.h
