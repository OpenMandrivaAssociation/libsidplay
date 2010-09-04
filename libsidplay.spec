%define major 1
%define libname %mklibname sidplay %{major}
%define develname %mklibname sidplay -d

Summary:	A Commodore 64 music player and SID chip emulator library
Name:		libsidplay
Version:	1.36.60
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Libraries
URL:		http://home.arcor.de/ms2002sep/bak/
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
 
%description
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it
you can play musics from Commodore 64 (or compatible) programs.

%package -n	%{libname}
Summary:	A Commodore 64 music player and SID chip emulator library
Group:		System/Libraries
Provides:	%{name} = %{version}

%description -n	%{libname}
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it
you can play musics from Commodore 64 (or compatible) programs.

%package -n	%{develname}
Summary:	Libraries and include files for developing libsidplay applications
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	sidplay-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname sidplay 1 -d}

%description -n	%{develname}
This package contains the header files and the static library for compiling
applications that use libsidplay. 

%prep

%setup -q

%build

%configure2_5x \
    --enable-optfixpoint \
    --enable-optendian

%make

%install
rm -rf %{buildroot}

%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}
 
%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc DEVELOPER src/*.txt
%{_includedir}/sidplay/
%{_libdir}/*.so
%{_libdir}/*a
