Summary:	Extra themes for GNOME 2 enviroment
Summary(pl):	Dodatkowe motywy dla środowiska GNOME 2
Name:		gnome-themes-extras
Version:	0.7
Release:	2
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	5069fedb0d8404c89d98fe8de6825bca
URL:		http://www.gnome.org/
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool >= 0.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of extra themes for the GNOME 2 desktop.

%description -l pl
Pakiet zawiera zestaw dodatkowych motywów dla środowiska GNOME 2.

%package Amaranth
Summary:	Amaranth theme for GNOME 2 enviroment
Summary(pl):	Motyw Amaranth dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Amaranth
Amaranth theme for GNOME 2 enviroment.

%description Amaranth -l pl
Motyw Amaranth dla środowiska GNOME 2.

%package Gorilla
Summary:	Gorilla theme for GNOME 2 enviroment
Summary(pl):	Motyw Gorilla dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-theme-engine-Industrial

%description Gorilla
Gorilla theme for GNOME 2 enviroment.

%description Gorilla -l pl
Motyw Gorilla dla środowiska GNOME 2.

%package Lush
Summary:	Lush theme for GNOME 2 enviroment
Summary(pl):	Motyw Lush dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Lush
Lush theme for GNOME 2 enviroment.

%description Lush -l pl
Motyw Lush dla środowiska GNOME 2.

%package Nuvola
Summary:	Nuvola theme for GNOME 2 enviroment
Summary(pl):	Motyw Nuvola dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Nuvola
Nuvola theme for GNOME 2 enviroment.

%description Nuvola -l pl
Motyw Nuvola dla środowiska GNOME 2.

%package Wasp
Summary:	Wasp theme for GNOME 2 enviroment
Summary(pl):	Motyw Wasp dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Wasp
Wasp theme for GNOME 2 enviroment.

%description Wasp -l pl
Motyw Wasp dla środowiska GNOME 2.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
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

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/lib*.so

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
