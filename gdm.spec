%define ver     1.0.0
%define rel      2
%define prefix  /usr

Summary: GNOME Display Manager
Name: gdm
Version: %ver
Release: %rel
Source: ftp://ftp.socsci.auc.dk/pub/empl/mkp/gdm-%{PACKAGE_VERSION}.tar.gz
Group: X11/Utilities
Copyright: LGPL/GPL
BuildRoot:	/tmp/%{name}-%{version}-root
Prefix: %{prefix}
Docdir: %{prefix}/doc
Requires: gnome-libs >= 1.0.0

%description 
gdm manages local and remote displays and provides the user with a
graphical login window.

%prep
%setup

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
	CFLAGS="$RPM_OPT_FLAGS" \
	./autogen.sh %{_target} \
		--prefix=%prefix
else
	CFLAGS="$RPM_OPT_FLAGS" \
	./configure %{_target} \
		--prefix=%prefix
fi
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install

strip $RPM_BUILD_ROOT%{prefix}/bin/* || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO docs/gdm-manual.txt
%defattr(-, gdm, gdm) 
%{prefix}/bin/gdm
%{prefix}/bin/gdmgreeter
%{prefix}/bin/gdmchooser
%attr (750, gdm, gdm) %{prefix}/var/gdm
%attr (-,root,root) %{prefix}/share/locale/*/*
%config %{prefix}/etc/gdm
%config %{prefix}/etc/gnomerc
