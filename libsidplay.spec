%define name libsidplay
%define version 1.36.59
%define release %mkrel 1
%define major 1
%define libname %mklibname sidplay %major

Summary: A Commodore 64 music player and SID chip emulator library.
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Libraries
Source: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-%{version}.tar.bz2
Icon: sidplay.xpm
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/linux.html
 
%description
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it
you can play musics from Commodore 64 (or compatible) programs.

%package -n %libname
Summary: A Commodore 64 music player and SID chip emulator library.
Group: System/Libraries
Provides: %{name} = %{version}

%description -n %libname
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it
you can play musics from Commodore 64 (or compatible) programs.


%package -n %libname-devel
Summary: Libraries and include files for developing libsidplay applications.
Group: Development/C++
Requires: %libname = %{version}-%release
Provides: %{name}-devel = %{version}-%release
Provides: sidplay-devel = %{version}-%release

%description -n %{libname}-devel
This package contains the header files and the static library for compiling
applications that use libsidplay. 

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%configure2_5x --enable-optfixpoint --enable-optendian

%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig
 
%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/lib*.so.*
%files -n %{libname}-devel
%defattr(-,root,root)
%doc DEVELOPER src/*.txt
%{_includedir}/sidplay/
%{_libdir}/*.so
%{_libdir}/*a


