Summary:	Extra themes for GNOME 2 enviroment
Summary(pl):	Dodatkowe motywy dla ¶rodowiska GNOME 2
Name:		gnome-themes-extras
Version:	0.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	04e0563d298b8419106813b1db0b15b0
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gnome.org/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	intltool >= 0.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of extra themes for the GNOME 2 desktop.

%description -l pl
Pakiet zawiera zestaw dodatkowych motywów dla ¶rodowiska GNOME 2.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gnome-themes-extra

# no *.la for gtk engine modules
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gnome-themes-extra.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/lib*.so
%{_datadir}/icons/*
%{_datadir}/themes/*
