%define major 1
%define libname %mklibname sidplay %{major}
%define devname %mklibname sidplay -d
%define _disable_lto 1

Summary:	A Commodore 64 music player and SID chip emulator library
Name:		libsidplay
Version:	1.36.60
Release:	16
License:	GPLv2+
Group:		System/Libraries
Url:		http://home.arcor.de/ms2002sep/bak/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libsidplay-1.36.60-c++17.patch
 
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

%package -n	%{devname}
Summary:	Libraries and include files for developing libsidplay applications
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	sidplay-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the header files and the static library for compiling
applications that use libsidplay. 

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--enable-optfixpoint \
	--enable-optendian

%make

%install
%make_install

%files -n %{libname}
%{_libdir}/libsidplay.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING
%doc DEVELOPER src/*.txt
%{_includedir}/sidplay/
%{_libdir}/*.so

