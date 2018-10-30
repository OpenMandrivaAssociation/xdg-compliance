%define _disable_rebuild_configure 1

Summary:	Packages to help old desktop environments follow XDG standards
Name:		xdg-compliance
Version:	0.1
Release:	18
License:	MIT
Group:		Graphical desktop/Other
URL:		http://gitorious.org/xdg-autostart/
Source0:	xdg-autostart-%{version}.tar.bz2
Source1:	xdg-autostart.xinit
Source2:	update-menus.xinit
Patch0:		xdg-autostart-0.1-gcc4.7.patch
Patch1:		xdg-autostart-autostart-fail.patch
Patch2:		xdg-autostart-0.1-OtherDEs.patch
Patch3:		xdg-autostart-0.1-look_first_sysconfdir.patch
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
%setup -q -n xdg-autostart-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

install -D -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xinit.d/xdg-autostart
install -D -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/X11/xinit.d/update-menus
