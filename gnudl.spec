%define         srcname       gdl
# imagemagick version insufficient in mdv < 2012
%if %mdkversion >= 201200
%define         withMagic     yes
%else
%define         withMagic     no
%endif

Name:           gnudl
Version:        0.9.2
Release:        2
Summary:        A free incremental compiler quite similar and compatible with IDL
License:        GPLv2+
Group:          Development/Other

URL:            https://gnudatalanguage.sourceforge.net/
Source0:        http://sourceforge.net/projects/gnudatalanguage/files/gdl/%{version}/%{srcname}-%{version}.tar.gz


BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libgomp-devel
BuildRequires:  readline-devel
BuildRequires:  libwxgtku-devel
BuildRequires:  ncurses-devel
BuildRequires:  gsl-devel
BuildRequires:  plplot-devel
BuildRequires:  netcdf-devel
BuildRequires:  proj4-devel
BuildRequires:  hdf5-devel
BuildRequires:  fftw-devel
BuildRequires:  udunits2-devel
BuildRequires:  jpeg-devel
BuildRequires:  pslib-devel
%if %mdkversion >= 201200
BuildRequires:  imagemagick-devel
%endif

%description
A free compatible incremental compiler (i.e. runs Interactive Data
Language programs). IDL is a registered trademark of ITT Visual
Information Solutions. All IDL language elements up to IDL version 7.1
are supported and more than 380 library routines are implemented. For
a sorted list enter HELP,/LIB at the command prompt and look for
library routines written in GDL in the gnudatalanguage/lib directory.


%prep
%setup -q -n %{srcname}-%{version}


%build
autoreconf --force --install
%configure2_5x  --with-Magick=%{withMagic}    \
                --with-hdf=no        \
                --with-fftw=yes      \
                --with-python=no     \
                --with-wxWidgets     \
                --with-udunits
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS TODO HACKING ChangeLog COPYING
%{_mandir}/man1/*
%{_bindir}/gdl
%{_datadir}/gnudatalanguage/*



%changelog
* Sat May 26 2012 Frank Kober <emuse@mandriva.org> 0.9.2-1mdv2011.0
+ Revision: 800767
- backport to 2011 doesn't support Magick either
- backport to 2010.1 doesn't support Magick
- revert gomp-devel BR to libgomp-devel for backports

* Fri May 25 2012 Frank Kober <emuse@mandriva.org> 0.9.2-1
+ Revision: 800555
- imported package gnudl

