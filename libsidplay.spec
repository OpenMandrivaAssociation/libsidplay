%define major 1
%define libname %mklibname sidplay %{major}
%define develname %mklibname sidplay -d

Summary:	A Commodore 64 music player and SID chip emulator library
Name:		libsidplay
Version:	1.36.60
Release:	%mkrel 4
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


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.36.60-2mdv2011.0
+ Revision: 660281
- mass rebuild

* Sat Sep 04 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.36.60-1mdv2011.0
+ Revision: 575878
- new version
- new URL
- drop patch

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.36.59-9mdv2010.1
+ Revision: 520907
- rebuilt for 2010.1

* Fri May 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.36.59-8mdv2010.0
+ Revision: 378681
- update license

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.36.59-7mdv2009.0
+ Revision: 229856
- fix build (opensuse)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.36.59-5mdv2008.1
+ Revision: 178946
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1.36.59-3mdv2008.0
+ Revision: 76980
- cleanup borked deps
- cleanup borked deps

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1.36.59-2mdv2008.0
+ Revision: 76880
- new devel naming

  + Thierry Vignaud <tv@mandriva.org>
    - kill icon tag


* Sun Jan 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.36.59-1mdv2007.0
+ Revision: 114682
- Import libsidplay

* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 1.36.59-1mdv2007.1
- rebuild

* Wed Aug 18 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.36.59-1mdk
- New release 1.36.59

* Sat Jul 24 2004 Götz Waschk <waschk@linux-mandrake.com> 1.36.58-1mdk
- autoconf 2.5 macro
- drop all patches
- New release 1.36.58

* Sat Jun 05 2004 Götz Waschk <waschk@linux-mandrake.com> 1.36.57-7mdk
- patch to make it build with g++ 3.4
- include debian patch
- fix URLs

