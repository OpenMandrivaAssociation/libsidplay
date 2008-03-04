%define major 1
%define libname %mklibname sidplay %{major}
%define develname %mklibname sidplay -d

Summary:	A Commodore 64 music player and SID chip emulator library
Name:		libsidplay
Version:	1.36.59
Release:	%mkrel 5
License:	GPL
Group:		System/Libraries
URL:		http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/linux.html
Source:		http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
 
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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
