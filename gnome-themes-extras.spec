Summary:	Extra themes for GNOME 2 enviroment
Summary(pl.UTF-8):	Dodatkowe motywy dla środowiska GNOME 2
Name:		gnome-themes-extras
Version:	2.20
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	830b27cb368e40c70b15288d2db12937
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gtk2-engines >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
Obsoletes:	gnome-themes-extras-Amaranth
Obsoletes:	gnome-themes-extras-Gorilla
Obsoletes:	gnome-themes-extras-Lush
Obsoletes:	gnome-themes-extras-Nuvola
Obsoletes:	gnome-themes-extras-Wasp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of extra themes for the GNOME 2 desktop.

%description -l pl.UTF-8
Pakiet zawiera zestaw dodatkowych motywów dla środowiska GNOME 2.

%package Darklooks
Summary:	Darklooks theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Darklooks dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Darklooks
Darklooks theme for GNOME 2 enviroment.

%description Darklooks -l pl.UTF-8
Motyw Darklooks dla środowiska GNOME 2.

%package Foxtrot
Summary:	Foxtrot theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Foxtrot dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Foxtrot
Foxtrot theme for GNOME 2 enviroment.

%description Foxtrot -l pl.UTF-8
Motyw Foxtrot dla środowiska GNOME 2.

%package Gion
Summary:	Gion theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Gion dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Gion
Gion theme for GNOME 2 enviroment.

%description Gion -l pl.UTF-8
Motyw Gion dla środowiska GNOME 2.

%package Neu
Summary:	Neu theme for GNOME 2 enviroment
Summary(pl.UTF-8):	Motyw Neu dla środowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Neu
Neu theme for GNOME 2 enviroment.

%description Neu -l pl.UTF-8
Motyw Neu dla środowiska GNOME 2.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for dir in Foxtrot Gion Neu
do
    gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/$dir
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files Darklooks
%defattr(644,root,root,755)
%{_datadir}/themes/Darklooks

%files Foxtrot
%defattr(644,root,root,755)
%{_iconsdir}/Foxtrot

%files Gion
%defattr(644,root,root,755)
%{_iconsdir}/Gion

%files Neu
%defattr(644,root,root,755)
%{_iconsdir}/Neu
