%define _disable_rebuild_configure 1

Summary:	Packages to help old desktop environments follow XDG standards
Name:		xdg-compliance
Version:	1.3.1
Release:	1
License:	MIT
Group:		Graphical desktop/Other
URL:		https://gitlab.com/somini/xdg-autostart
Source0:	https://gitlab.com/somini/xdg-autostart/-/archive/v%{version}/xdg-autostart-v%{version}.tar.bz2
Source1:	xdg-autostart.xinit
Source2:	update-menus.xinit

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)

Requires:	%{name}-autostart
Requires:	%{name}-menu

%description
This meta-package requires %{name}-autostart and %{name}-menu.

%files

#------------------------------------------------------------------------------#

%package autostart
Summary:	XDG Autostart compliance for old desktop environments
Group:		Graphical desktop/Other

%description autostart
This package provides a xinit.d script that emulates XDG Autostart compliance
for old desktop environments.

%files autostart
%{_bindir}/xdg-autostart
%{_sysconfdir}/X11/xinit.d/xdg-autostart

#------------------------------------------------------------------------------#

%package menu
Summary:	User menus for old desktop environments based on XDG Menu
Group:		Graphical desktop/Other

%description menu
This package creates user-level menus for old desktop environments following
the XDG Menu standard.

%files menu
%{_sysconfdir}/X11/xinit.d/update-menus

#------------------------------------------------------------------------------#

%prep
%autosetup -p1 -n xdg-autostart-%{version}

%build
%meson
%meson_build

%install
%meson_install

install -D -m 755 build/xdg-autostart %{buildroot}%{_bindir}/xdg-autostart
install -D -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xinit.d/xdg-autostart
install -D -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/X11/xinit.d/update-menus
