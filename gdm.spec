%define ver     2.0.0
%define rel     1
%define prefix  /usr

Summary:     GNOME Display Manager
Name:        gdm
Version:     %ver
Release:     %rel
Source:      ftp://ftp.socsci.auc.dk/pub/empl/mkp/gdm-%{PACKAGE_VERSION}.tar.gz
Patch:       gdm-correct.patch
Group:       X11/Utilities
Copyright:   LGPL/GPL
BuildRoot:   /tmp/%{name}-%{version}-root
Prefix:      %{prefix}
Docdir:      %{prefix}/doc
Requires:    gnome-libs >= 1.0.0

%description 
gdm manages local and remote displays and provides the user with a
graphical login window.

%prep
%setup -q
%patch -p1

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
	CFLAGS="$RPM_OPT_FLAGS" \
	./autogen.sh \
		--prefix=%prefix \
		--sysconfdir=/etc/X11
else
	CFLAGS="$RPM_OPT_FLAGS" \
	./configure \
		--prefix=%prefix \
		--sysconfdir=/etc/X11
fi

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{prefix},etc/pam.d,etc/X11}
make prefix=$RPM_BUILD_ROOT%{prefix} \
     authdir=$RPM_BUILD_ROOT/var/gdm \
     sysconfdir=$RPM_BUILD_ROOT/etc/X11 install
install  $RPM_BUILD_DIR/%{name}-*/config/gdm $RPM_BUILD_ROOT/etc/pam.d

strip $RPM_BUILD_ROOT%{prefix}/bin/* || :

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if ! `grep gdm /etc/passwd >/dev/null 2>&1`; then
    if ! `grep gdm /etc/group >/dev/null 2>&1`; then
	groupadd -g 60 -f gdm >/dev/null 2>&1 || :
    fi
    useradd -M -o -r -d /var/gdm -g gdm -u 60 -s /bin/bash \
	-c "gdm user" gdm >/dev/null 2>&1 || :
fi

%files
%doc AUTHORS ChangeLog NEWS README TODO docs/gdm-manual.txt
%defattr(644, root, root, 755) 
%config %attr (755, root, root) /etc/X11/gdm/Init
%config %attr (755, root, root) /etc/X11/gdm/Sessions
%config /etc/X11/gdm/gdm.conf
%config /etc/X11/gdm/locale.alias
%config %attr (755, root, root) /etc/X11/gnomerc
/etc/pam.d/gdm
%attr (750, root, root) %{prefix}/bin/gdm
%attr (750, root, root) %{prefix}/bin/gdmgreeter
%attr (750, root, root) %{prefix}/bin/gdmchooser
%attr (750, root, root) %{prefix}/bin/gdmlogin
%attr (750, gdm, gdm)   /var/gdm
%{prefix}/share/locale/*/*
%{prefix}/share/pixmaps/*
