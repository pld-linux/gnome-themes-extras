Summary:	Extra themes for GNOME 2 enviroment
Summary(pl.UTF-8):	Dodatkowe motywy dla środowiska GNOME 2
Name:		gnome-themes-extras
Version:	0.9.0
Release:	2
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	bac18c11fb9de8403e27441be64d9717
Patch0:		%{name}-locale_names.patch
Patch1:		%{name}-nuvola.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gnome-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of extra themes for the GNOME 2 desktop.

%description -l pl.UTF-8
Pakiet zawiera zestaw dodatkowych motywów dla środowiska GNOME 2.

%package Amaranth
Summary:	Amaranth theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Amaranth dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-engines >= 2.6.1

%description Amaranth
Amaranth theme for GNOME 2 enviroment.

%description Amaranth -l pl.UTF-8
Motyw Amaranth dla środowiska GNOME 2.

%package Gorilla
Summary:	Gorilla theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Gorilla dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-engines >= 2.6.1

%description Gorilla
Gorilla theme for GNOME 2 enviroment.

%description Gorilla -l pl.UTF-8
Motyw Gorilla dla środowiska GNOME 2.

%package Lush
Summary:	Lush theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Lush dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-engines >= 2.6.1

%description Lush
Lush theme for GNOME 2 enviroment.

%description Lush -l pl.UTF-8
Motyw Lush dla środowiska GNOME 2.

%package Nuvola
Summary:	Nuvola theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Nuvola dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-engines >= 2.6.1

%description Nuvola
Nuvola theme for GNOME 2 enviroment.

%description Nuvola -l pl.UTF-8
Motyw Nuvola dla środowiska GNOME 2.

%package Wasp
Summary:	Wasp theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Wasp dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-engines >= 2.6.1

%description Wasp
Wasp theme for GNOME 2 enviroment.

%description Wasp -l pl.UTF-8
Motyw Wasp dla środowiska GNOME 2.

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

for dir in Amaranth Gorilla Lush Nuvola Wasp
do
    gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/$dir
done

%find_lang %{name}

# no *.la for gtk engine modules
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/lib*.la

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
