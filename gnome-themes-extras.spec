Summary:	Extra themes for GNOME 2 enviroment
Summary(pl):	Dodatkowe motywy dla ¶rodowiska GNOME 2
Name:		gnome-themes-extras
Version:	0.8.0
Release:	2
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	a2c3eead4dd29bad88b57570d67afd33
Patch0:		%{name}-locale_names.patch
Patch1:		%{name}-nuvola.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libtool
Requires:	gnome-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of extra themes for the GNOME 2 desktop.

%description -l pl
Pakiet zawiera zestaw dodatkowych motywów dla ¶rodowiska GNOME 2.

%package Amaranth
Summary:	Amaranth theme for GNOME 2 enviroment
Summary(pl):	Motyw Amaranth dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-theme-engine-Smooth

%description Amaranth
Amaranth theme for GNOME 2 enviroment.

%description Amaranth -l pl
Motyw Amaranth dla ¶rodowiska GNOME 2.

%package Gorilla
Summary:	Gorilla theme for GNOME 2 enviroment
Summary(pl):	Motyw Gorilla dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-theme-engine-Industrial

%description Gorilla
Gorilla theme for GNOME 2 enviroment.

%description Gorilla -l pl
Motyw Gorilla dla ¶rodowiska GNOME 2.

%package Lush
Summary:	Lush theme for GNOME 2 enviroment
Summary(pl):	Motyw Lush dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-theme-engine-Smooth

%description Lush
Lush theme for GNOME 2 enviroment.

%description Lush -l pl
Motyw Lush dla ¶rodowiska GNOME 2.

%package Nuvola
Summary:	Nuvola theme for GNOME 2 enviroment
Summary(pl):	Motyw Nuvola dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-theme-engine-Smooth

%description Nuvola
Nuvola theme for GNOME 2 enviroment.

%description Nuvola -l pl
Motyw Nuvola dla ¶rodowiska GNOME 2.

%package Wasp
Summary:	Wasp theme for GNOME 2 enviroment
Summary(pl):	Motyw Wasp dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-theme-engine-Smooth

%description Wasp
Wasp theme for GNOME 2 enviroment.

%description Wasp -l pl
Motyw Wasp dla ¶rodowiska GNOME 2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po

%build
%{__aclocal} -I m4
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

# no *.la for gtk engine modules
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/lib*.la

# Industrial are in gtk2-theme-engine-Industrial
# but gorilla depends on libindustrial.so
rm -rf $RPM_BUILD_ROOT%{_datadir}/themes/Industrial
rm  -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/libindustrial.so

# Smooth engine is in gtk2-theme-engine-Smooth
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/libsmooth.so

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%files Amaranth
%defattr(644,root,root,755)
%{_datadir}/icons/Amaranth
%{_datadir}/themes/Amaranth

%files Gorilla
%defattr(644,root,root,755)
%{_datadir}/icons/Gorilla
%{_datadir}/themes/Gorilla

%files Lush
%defattr(644,root,root,755)
%{_datadir}/icons/Lush
%{_datadir}/themes/Lush

%files Nuvola
%defattr(644,root,root,755)
%{_datadir}/icons/Nuvola
%{_datadir}/themes/Nuvola*

%files Wasp
%defattr(644,root,root,755)
%{_datadir}/icons/Wasp
%{_datadir}/themes/Wasp
