%define         srcname       gdl

Name:           gnudl
Version:        0.9.2
Release:        %mkrel 1
Summary:        A free incremental compiler quite similar and compatible with IDL
License:        GPLv2+
Group:          Development/Other

URL:            http://gnudatalanguage.sourceforge.net/
Source0:        http://sourceforge.net/projects/gnudatalanguage/files/gdl/%{version}/%{srcname}-%{version}.tar.gz


BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gomp-devel
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
BuildRequires:  imagemagick-devel


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
%configure2_5x  --with-Magick=yes    \
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

